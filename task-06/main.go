package main

import (
	"context"
	"fmt"
	"log"
	"net/http"

	"github.com/vartanbeno/go-reddit/reddit"
)

var ctx = context.Background()

func main() {
	if err := run(); err != nil {
		log.Fatal(err)
	}
}

func run() (err error) {

	withCredentials := reddit.WithCredentials("##########", "########################", "###########", "##########")
	client, _ := reddit.NewClient(withCredentials)
	if err != nil {
		return
	}

	client.OnRequestCompleted(logResponse)

	subreddits, _, err := reddit.DefaultClient().Subreddit.SearchNames(ctx, "memes")
	fmt.Println(subreddits)

	sr, _, err := reddit.DefaultClient().Subreddit.Get(ctx, "memes")
	fmt.Printf("%s was created on %s and has %d subscribers.\n", sr.NamePrefixed, sr.Created.Local(), sr.Subscribers)

	posts, _, err := client.Subreddit.TopPosts(context.Background(), "memes", &reddit.ListPostOptions{
		ListOptions: reddit.ListOptions{
			Limit: 100,
		},
		Time: "week",
	})
	if err != nil {
		return err
	}

	for _, post := range posts {
		_, err = client.Post.Upvote(context.Background(), post.FullID)
		if err != nil {
			return err
		}
	}

	return
}

func logResponse(req *http.Request, res *http.Response) {
	fmt.Printf("%s %s %s\n", req.Method, req.URL, res.Status)
}
