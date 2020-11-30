msg = "Hi";
time = 1  ; 
times = 10 ;
a = 0 ;
spammsg = setInterval(function(){
document.getElementsByClassName('composer_rich_textarea')[0].innerHTML = msg;
$('.im_submit_send').trigger('mousedown');	
a++;

if( a  === times )
clearInterval(spammsg);
} , time * 1000 ) ;