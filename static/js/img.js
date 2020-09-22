$(function() {
    $("#upload_btn").click(function() {
        let fs = $('#file_input')[0].files
        if (fs.length == 0) {
            alert("未选择文件")
        } else if (fs.length > 1) {
            alert("暂不支持上传多文件")
        } else {
            $.ajax({
                url: '/api/upload_img',
                type: 'POST',
                cache: false,
                data: new FormData($('#upload_file_form')[0]),
                processData: false,
                contentType: false,
                success: function(resp) {
                    console.log(resp)
                }
            })
        }
    })
})
