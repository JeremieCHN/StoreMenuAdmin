$(function() {
    $("#username").click(function() {
        console.log("click")
        $.ajax({
            url: '/api/logout',
            type: 'GET'
        }).done(function() {
            window.location = '/admin/login'
        })
    })
})
