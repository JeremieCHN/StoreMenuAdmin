
// 新增类型相关的部分
function init_img_selector() {
    const on_net_fail = function (err) {
        console.log(err)
        show_err("拉取图片失败，请刷新重试")
    }
    $.ajax({
        url: "/api/get_img_list",
        type: "GET",
        success: function (resp) {
            resp = JSON.parse(resp)
            if (resp.code != 0) {
                on_net_fail()
            } else {
                var data = JSON.parse(resp.data)
                image_data = data
                for (var img of data) {
                    var id = `img-option-${img.id}`
                    $("#type-img-select").append(`<option id="${id}">${img.id}</option>`)
                    $("#" + id).attr("data-content",
                        `<div class='row align-items-center'>
                            <div class='col-auto'>
                                <img src='/api/images/${img.filename}' width='80px' height='80px'>
                            </div>
                            <div class='col'>
                                <h5 class='mt-0'>原文件名：${img.origin_filename}</h5>
                                <span class='text-dark'>ID:${img.id}</span>
                            </div>
                        </div>`)
                }
                $('#type-img-select').selectpicker('refresh');
                $("#new-type-btn").attr("disabled", false)
                bind_new_type_btns()
            }
        },
        fail: on_net_fail
    })
}

function bind_new_type_btns() {
    $("#new-type-btn").click(function () {
        $("#add-type-modal").modal("show")
    })

    $("#save-btn").click(function () {
        var typename = $("#type-name-input").val()
        var img = $("#type-img-select").selectpicker('val')
        var order = $("#type-order-input").val()

        if (typename.length == 0) {
            show_err("请输入类型名")
        } else if (img.length == 0) {
            show_err("请选择图片，如果没有需要先行添加图片")
        } else if (order.length == 0) {
            show_err("请输入顺序号")
        } else {
            show_loading("上传数据中")
            img = Number(img)
            $.ajax({
                url: "/api/add_type",
                type: "POST",
                contentType: "application/json;charset=utf-8",
                data: JSON.stringify({
                    "type_name": typename,
                    "img_id": img,
                    "show_index": order
                }),
                success: function(resp) {
                    console.log(resp)
                    resp = JSON.parse(resp)
                    close_loading()
                    if (resp.code == 0) {
                        close_loading()
                        $("#add-type-modal").modal("hide")
                        $("#type-name-input").val("")
                        $("#type-img-select").selectpicker('val', "")
                        $("#type-order-input").val(1)
                        show_info("新增成功", function() {
                            location.reload();
                        })
                    } else {
                        show_err("失败：" + JSON.stringify(resp))
                    }
                },
                fail: function (err) {
                    close_loading()
                    show_err("意外失败，请刷新重试")
                    console.log(err)
                }
            })
        }
    })
}

// 主要显示部分
var type_data, cur_page

function init_type_list() {
    $.ajax({
        url: "/api/get_type_list",
        type: "GET",
        success: function (resp) {
            var _resp = resp
            resp = JSON.parse(resp)
            if (resp.code != 0) {
                show_err("拉取类型列表失败，请刷新重试: "+ _resp)
            } else {
                data = JSON.parse(resp.data)
                data.sort(function(t1, t2) {
                    if (t1.show_index != t2.show_index) {
                        return t1.show_index - t2.show_index
                    } else {
                        return t1.id - t2.id
                    }
                })
                type_data = data
                page_count = Math.ceil(data.length / 10)

                tempatePagination(page_count)
                on_page_click(1)
            }
        },
        fail: function() {
            show_err("拉取类型列表失败，请刷新重试")
        }
    })
}

function tempatePagination(page_count) {
    for (var i = 2; i <= page_count; i++) {
        $("#pagination-next").insertBefore(
            `<li class="page-item deactive"><span onclick="on_page_click(${i})" class="page-link">${i}</span></li>`
        )
    }
}

function tempatePage(page) {
    $("#type-table-body").empty()
    var start = (page - 1) * 10
    var end = Math.min(type_data.length - 1, start + 10 - 1)
    for (var i = start; i <= end; i++) {
        $("#type-table-body").append(tempateType(type_data[i]))
    }
}

function on_page_click(page) {
    var page_count = Math.ceil(type_data.length / 10)
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

function tempateType(item) {
    return `
    <tr>
        <td>${item.id}</td>
        <td>${item.type_name}</td>
        <td style="width:100px; height:100px">
            <img src="/api/images_id/${item.img_id}" />
        </td>
        <td><button class="btn btn-danger" onclick="on_click_remove(${item.id})">删除</button></td>
    </tr>
    `
}

function on_click_remove(type_id) {
    console.log(type_id)
    show_info("后续再做吧")
}

$(function () {
    init_img_selector()
    init_type_list()
    $("#type-order-input").val(1)
})
