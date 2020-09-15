window.onload = function() {
    $("#login_btn").click(function() {
        let username = $("#username").val()
        let password = $("#password").val()
        if (username == undefined || password == undefined) {
            alert("输入少了")
            return true
        }

        $.ajax({
            url: "/api/login",
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify({ username: username, password: password }),
            success: function(resp) {
                let res = JSON.parse(resp)
                if (res.code == 0)
                    window.location = '/'
                else
                    alert("登录失败")
            }
        })
    })
}
