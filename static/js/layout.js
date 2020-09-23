$(function () {
    $("#logout-btn").click(function () {
        console.log("click")
        $.ajax({
            url: '/api/logout',
            type: 'GET'
        }).done(function () {
            window.location = '/admin/login'
        })
    })
    $("#loading-modal").modal({
        backdrop: "static",
        keyboard: false,
        show: false
    })
})

function show_err(msg) {
    $("#dialog-title").html("<span class='text-danger'>错误</span>")
    $("#dialog-message").text(msg)
    $("#alert-modal").modal()
}

function show_info(msg, callback) {
    if (typeof callback !== 'undefined') {
        $("#alert-modal").on('hidden.bs.modal', callback)
    }
    $("#dialog-title").html("提示")
    $("#dialog-message").text(msg)
    $("#alert-modal").modal()
}

function show_loading(msg) {
    $("#loading-message").text(msg)
    $("#loading-modal").modal("show")
}

function close_loading() {
    $("#loading-modal").modal("hide")
}
