timelag = 1; 
times = 10;
ittrate = 0;
spammsg = setInterval(function(){
document.getElementsByClassName('composer_rich_textarea')[0].innerHTML = "Hi";
$('.im_submit_send').trigger('mousedown');	
ittrate++;

if( ittrate  === times )
clearInterval(spammsg);
} , timelag * 1000 ) ;
