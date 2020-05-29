function add(toAdd,a) {
    const c = "add/" + a + ".html";
    $.get(c, function (data, status) {
        alert("数据: " + data + "\n状态: " + status);

    });
    // toAdd.values= "已关注";
    //  alert(toAdd.innerHTML);
    // $(toAdd).attr({"value":"已关注"});
}




