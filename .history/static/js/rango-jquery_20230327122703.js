$(document).ready(function() {
    // alert('Hello, world!');

    $('#about-btn').click(function() {
        alert('You clicked the button using JQuery!')
    });

    $('#about-btn').click(function() {
        msgStr = $('#msg').html();
        msgStr = msgStr + ' ooo, fancy!';

        $('#msg').html(msgStr);
    });
});