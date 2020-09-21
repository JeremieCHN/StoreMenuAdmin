window.onload = function() {

    $("#login_btn").click(function() {
        $("#login_btn").attr("disabled", true);

        let username = $("#username").val()
        let password = $("#password").val()
        if (username.length == 0) {
            $("[role='alert'] > span").text("eee")
            $("[role='alert']").alert()
        }

        $("#login_btn").attr("disabled", false);


        // if (username == undefined || password == undefined) {
        //     alert("输入少了")
        //     return true
        // }

        // $.ajax({
        //     url: "/api/login",
        //     type: "POST",
        //     contentType: "application/json",
        //     data: JSON.stringify({ username: username, password: password }),
        //     success: function(resp) {
        //         let res = JSON.parse(resp)
        //         if (res.code == 0)
        //             window.location = '/admin'
        //         else
        //             alert("登录失败")
        //     }
        // })
    })
}
