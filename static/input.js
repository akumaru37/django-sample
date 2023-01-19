// 画面がロードされたら実行
$(document).ready(e => {
    // #aでelementを指定、それのblurでフォーカスが離れたら！
    $("#a").blur(be => {
        // beはイベントが実行された時のイベントオブジェクト、そのtargetに発火したelementが入っているので、jqueryのObjにしてから、入力値をvalで取り出す
        var aval = $(be.target).val();
        // 自動入力するやつにclass="d"をつけてあるので、.dで複数取得して、eachで回す。idxは1つ目、その場合のelementが2つ目
        $(".d").each((i, elem) => {
            // elemをjQueryのObjにしてからvalで値をセット
            $(elem).val(aval + "_" + i);
        });
    });
});
