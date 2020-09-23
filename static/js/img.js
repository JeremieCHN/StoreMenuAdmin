// 数据保存
var image_data = undefined
var cur_page = 1

// 渲染用
function tempateImage(item) {
    return `
    <tr>
        <td>${item.id}</td>
        <td>${item.origin_filename}</td>
        <td>${item.filename}</td>
        <td style="width:100px; height:100px">
            <img src="/api/images/${item.filename}" />
        </td>
        <td><button class="btn btn-danger" onclick="on_click_remove(${item.id})">删除</button></td>
    </tr>
    `
}

function tempatePagination(page_count) {
    for (var i = 2; i <= page_count; i++) {
        $("#pagination-next").insertBefore(
            `<li class="page-item deactive"><span onclick="on_page_click(${i})" class="page-link">${i}</span></li>`
        )
    }
}

function tempatePage(page) {
    $("#img-table-body").empty()
    var start = (page - 1) * 10
    var end = Math.min(image_data.length - 1, start + 10 - 1)
    for (var i = start; i <= end; i++) {
        $("#img-table-body").append(tempateImage(image_data[i]))
    }
}

function tempate_table() {
    var count = image_data.length
    var page_count = Math.ceil(count / 10)
    tempatePagination(page_count)
    on_page_click(cur_page)
}

// 相关监听事件

function on_click_remove(img_id) {
    console.log(img_id)
    show_info("后续再做吧")
}

function on_page_click(page) {
    var page_count = Math.ceil(image_data.length / 10)
    if (page > 0) {
        cur_page = page
    } else {
        if (page == -1) cur_page -= 1
        if (page == -1) cur_page += 1
        cur_page = Math.max(cur_page, 1)
        cur_page = Math.min(cur_page, page_count)
    }

    tempatePage(cur_page)
    var e = $("#pagination .active")
    e.removeClass("active")
    e.addClass("deactive")

    e = $("#pagination ul li:nth-child(" + (cur_page+1) + ")")
    e.addClass("active")
    e.removeClass("deactive")

    if (cur_page == 1) {
        $("#page-pre").addClass("disabled")
    } else {
        $("#page-pre").removeClass("disabled")
    }
    if (cur_page == page_count) {
        $("#page-next").addClass("disabled")
    } else {
        $("#page-next").removeClass("disabled")
    }
}

$(function() {

    // 上传相关的事件监听

    $("#file-chooser>input").change(function() {
        let fs = $('#file_input')[0].files
        if (fs.length > 0) {
            $("#filename").text("已选择：" + fs[0].name)
        }
    })
    $("#upload_btn").click(function() {
        let fs = $('#file_input')[0].files
        if (fs.length == 0) {
            show_err("未选择文件")
        } else if (fs.length > 1) {
            show_err("暂不支持上传多文件")
        } else {
            show_loading("上传中...")
            var data = new FormData()
            data.append("file", fs[0])
            $.ajax({
                url: '/api/upload_img',
                type: 'POST',
                cache: false,
                data: data,
                processData: false,
                contentType: false,
                success: function(resp) {
                    close_loading()
                    resp = JSON.parse(resp)
                    if (resp.code == 0) {
                        show_info("上传成功", function() {
                            location.reload();
                        })
                    } else {
                        show_err("上传失败，返回信息：" + resp)
                    }
                    console.log(resp)
                }
            })
        }
    })

    // 刷新数据

    show_loading("从服务器加载数据")
    $.ajax({
        url: "/api/get_img_list",
        type: 'GET',
        success: function (resp) {
            resp = JSON.parse(resp)
            if (resp.code != 0) {
                close_loading()
                show_err("拉取信息失败：" + resp)
            } else {
                var data = JSON.parse(resp.data)
                image_data = data
                tempate_table()
                close_loading()
            }
        }
    })
})
