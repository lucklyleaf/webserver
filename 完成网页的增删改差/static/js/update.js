function li1() {
    window.location.replace('/main.html');
    // window.location.href="main.html";
}
function li2(){
    window.location.href="/index.html";
}
function sub() {
    const bz = document.getElementById('bz');
    const num = document.getElementById('td2');
    const str = bz.value;
    const src = num.innerText + "/" + bz.value + ".html";
    if(str.length<=50){
        $.get(src, function (data, status){
            alert("数据: " + data + "\n状态: " + status);
            window.location.href = "/index.html";
        });
    }else {
        alert("不得高于五十个字符,请重新输入！");
    }

}

