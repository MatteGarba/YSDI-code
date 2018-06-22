var ip = "http://";
var score = 0;
var count = 0;

function hideInit(){
    $("#init").hide();
}

function requestUpdates(){
    $.getJSON(ip+"/jsData/tare",function (data) {
            var diz = data["values"];
            var val = diz["mic"];
            updateElements("mic-tare",val);
    });
    $.getJSON(ip+"/jsData/report",function (data) {
            var hc = data["history-count"];
            var mc = data["mic-count"];
            var sit = data["sit"];
            var remainingSeconds = data["remainingTime"];
            var t_a_b = data["TAB"];
            var pausing = data["pausing"];
            score = data["score"];
            updateElements("sites-number",hc);
            updateElements("speak-number",mc);
            updateElements("chair-last-bit",sit);
            updateElements("score",score);
            var b = $("#take-a-break");
            if (t_a_b === 1 || pausing === 1){
                b.css("diplay","block");
                if (t_a_b === 1){
                    b.text("You should definetely take a break.");
                }
                if (pausing===1){
                    var sec = remainingSeconds % 60;
                    remainingSeconds = remainingSeconds - sec;
                    var min = remainingSeconds / 60;
                    var st = "You still have ";
                    if (min < 10){
                        st = st + "0"
                    }
                    st = st + min + ":";
                    if (sec < 10){
                        st = st + "0";
                    }
                    st = st + sec + " minutes";
                    b.text(st);
                }
            }
            else{
                b.css("display","none");
            }
    });
}

function updateElements(id,val){
    $("#"+id).text(val);
}

function tare(){
    $("#init").show();
    setTimeout(function(){
            $("#init").hide()
        },3000);
    $.getJSON(ip+"/constants/tare");
}

function score(){
    $("#init").show();
    setTimeout(function(){
            $("#init").hide()
        },3000);
    $.getJSON(ip+"/constants/tare");
}

$(document).ready(function() {
        var v = setTimeout(hideInit,4000);
        $("#tare-button").click(tare);
        setInterval(requestUpdates,5000);

        var y = document.getElementById("ip");
        var x = y.getAttribute("myIp");
        ip = ip+x+':8080';
        document.getElementById("ip").style.display = "none";

        $("#break-button").click(function () {
            $(".breaks").toggleClass("active");
        })
        $("#break-spend-button").click(function(){
            $(".distractions").toggleClass("active");
        })
        $("#break-study-button").click(function(){
            $(".breaks").toggleClass("active");
        })
        $("#score-button").click(requestUpdates);
        $("#repeating-button").click(function () {
            $.getJSON(ip+"/functions/repeating", function (data){
                val = data["newScore"];
                updateElements("score",val);
            })
        })
        $("#stop-button").click(function () {
            $.get(ip + "/functions/stopStudying", function (data) {
                $("body").html(data);
            })
        })
        $("#score").click(function () {
            $(".debug").toggleClass("active");
        })
        $("#plus-button").click(function() {
            count = count + 1;
            $("#counter").text(count);
        })
        $("#minus-button").click(function () {
            if (count>0){
                count = count - 1;
            }
            $("#counter").text(count);
        })
        $(".info-of-service button").click(function () {
            $(".time-amount").toggleClass("active");
            $("#minute-number").text(score/10);
        })
        $("#confirm").click(function () {
            if (count > 0){
                if (score/10 >= count){
                    $.get(
                        ip+"/functions/pausing/"+count,
                        function(data){
                            score = data["newscore"];
                            updateElements("score", score);
                        }
                    )
                    $(".time-amount").toggleClass("active");
                    $(".distractions").toggleClass("active");
                }
                else{
                    alert("You don't have enough points!");
                }
                count = 0;
                $("#counter").text(count);
            }

        })

    }
);