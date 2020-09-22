window.onload = function() {

    $("#login_btn").click(function() {
        let username = $("#username").val()
        let password = $("#password").val()
        if (username.length == 0) {
            alert("用户名为空")
        } else if (password.length == 0) {
            alert("密码为空")
        } else {
            $("#login_btn").attr("disabled", true);
            $.ajax({
                url: "/api/login",
                type: "POST",
                contentType: "application/json",
                data: JSON.stringify({ username: username, password: password }),
                success: function(resp) {
                    let res = JSON.parse(resp)
                    if (res.code == 0)
                        window.location = '/admin'
                    else {
                        alert("登录失败，请检查用户名和密码")
                        $("#login_btn").attr("disabled", false);
                    }
                }
            })
        }
    })
}
