package main

import (
	"context"
	"fmt"
	"log"

	"github.com/vartanbeno/go-reddit/reddit"
)

var ctx = context.Background()

func main() {

	if err := run(); err != nil {
		log.Fatal(err)
	}
}

func run() (err error) {
	withCredentials := reddit.WithCredentials("id", "secrete", "username", "password")
	client, _ := reddit.NewReadonlyClient(withCredentials)
	// Let's get the top 200 posts of r/golang.
	// Reddit returns a maximum of 100 posts at a time,
	// so we'll need to separate this into 2 requests.
	posts, _, err := reddit.DefaultClient().Subreddit.TopPosts(ctx, "memes", &reddit.ListPostOptions{
		ListOptions: reddit.ListOptions{
			Limit: 100,
		},
		Time: "week",
	})

	if err != nil {
		return
	}
	for _, post := range posts {
		fmt.Println(post.Title)
		client.Post.Upvote(context.Background(), post.ID)
	}
	return
}
