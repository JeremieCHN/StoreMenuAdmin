// 子模块需要提供的
var dataset
var HeadHtml
var templateItem

// 给子模块的
const render_page = function () {
    $("#data-table-head").append(HeadHtml)
    var count = dataset.length
    var page_count = Math.ceil(count / 10)
    templatePagination(page_count)
    on_page_click(1)
}

// 本模块自身
var cur_page

function templatePagination(page_count) {
    for (var i = 2; i <= page_count; i++) {
        $("#pagination-next").insertBefore(
            `<li class="page-item deactive"><span onclick="on_page_click(${i})" class="page-link">${i}</span></li>`
        )
    }
}

function on_page_click(page) {
    var page_count = Math.ceil(dataset.length / 10)
    if (page > 0) {
        cur_page = page
    } else {
        if (page == -1) cur_page -= 1
        if (page == -1) cur_page += 1
        cur_page = Math.max(cur_page, 1)
        cur_page = Math.min(cur_page, page_count)
    }

    templatePage(cur_page)
    var e = $("#pagination .active")
    e.removeClass("active")
    e.addClass("deactive")

    e = $("#pagination ul li:nth-child(" + (cur_page + 1) + ")")
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

function templatePage(page) {
    $("#data-table-body").empty()
    var start = (page - 1) * 10
    var end = Math.min(dataset.length - 1, start + 10 - 1)
    for (var i = start; i <= end; i++) {
        console.log(dataset[i])
        $("#data-table-body").append(templateItem(dataset[i]))
    }
}
