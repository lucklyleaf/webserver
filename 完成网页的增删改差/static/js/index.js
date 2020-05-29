function del(a) {
    const str = "是否删除？\n\n请选择！";
    if(confirm(str)==true){
       const c = "del/" + a + ".html";
       $.get(c, function (data, status) {
               alert("数据: " + data + "\n状态: " + status);
               location.reload();
       });
        return true
    }else {
        return false
    }

}

