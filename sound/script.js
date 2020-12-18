function startInput() {
    document.getElementById("typebeat").focus();
}

var x = document.getElementById("myAudio");
var y = document.getElementById("myAudio2");
var z = document.getElementById("myAudio3");
var z2 = document.getElementById("myAudio4");
var a = document.getElementById("myAudio5");
var b = document.getElementById("myAudio6");
var c = document.getElementById("myAudio7");
var d = document.getElementById("myAudio8");
var e = document.getElementById("myAudio9");
var f = document.getElementById("myAudio10");
var g = document.getElementById("myAudio11");
var h = document.getElementById("myAudio12");
var i = document.getElementById("myAudio13");
var j = document.getElementById("myAudio14");
var k = document.getElementById("myAudio15");
var l = document.getElementById("myAudio16");
var m = document.getElementById("myAudio17");
var n = document.getElementById("myAudio18");
var o = document.getElementById("myAudio19");
var p = document.getElementById("myAudio20");
var q = document.getElementById("myAudio21");
var r = document.getElementById("myAudio22");
var t = document.getElementById("myAudio24");
var u = document.getElementById("myAudio25");
var v = document.getElementById("myAudio26");
var w = document.getElementById("myAudio27");
var w2 = document.getElementById("myAudio28");



var bg = document.getElementById("background");

function playAudio(e) {
    bg.style.backgroundColor = getRandomColor();

    if (e.key == ' ' || e.key == 'l' | e.key == '5') {
        z.pause();
        z.currentTime = 0;
        z.play();
        return;
    }
    if (e.key == 'a' || e.key == '6') {
        z2.pause();
        z2.currentTime = 0;
        z2.play();
        return;
    }
    if (e.key == 's' || e.key == '9') {
        x.pause();
        x.currentTime = 0;
        x.play();
        return;
    }
    if (e.key == 'd') {
        f.pause();
        f.currentTime = 0;
        f.play();
        return;
    }
    if (e.key == 'f') {
        g.pause();
        g.currentTime = 0;
        g.play();
        return;
    }
    if (e.key == 'g' || e.key == '8') {
        h.pause();
        h.currentTime = 0;
        h.play();
        return;
    }
    if (e.key == 'q') {
        a.pause();
        a.currentTime = 0;
        a.play();
        return;
    }
    if (e.key == 'w') {
        b.pause();
        b.currentTime = 0;
        b.play();
        return;
    }
    if (e.key == 'e' || e.key == '7') {
        c.pause();
        c.currentTime = 0;
        c.play();
        return;
    }
    if (e.key == 'r') {
        d.pause();
        d.currentTime = 0;
        d.play();
        return;
    }
    if (e.key == 't') {
        i.pause();
        i.currentTime = 0;
        i.play();
        return;
    }
    if (e.key == 'y') {
        j.pause();
        j.currentTime = 0;
        j.play();
        return;
    }
    if (e.key == 'u' || e.key == '2') {
        k.pause();
        k.currentTime = 0;
        k.play();
        return;
    }
    if (e.key == 'i' || e.key == '1') {
        l.pause();
        l.currentTime = 0;
        l.play();
        return;
    }
    if (e.key == 'z' || e.key == '0') {
        m.pause();
        m.currentTime = 0;
        m.play();
        return;
    }
    if (e.key == 'x' || e.key == '4') {
        n.pause();
        n.currentTime = 0;
        n.play();
        return;
    }
    if (e.key == 'c') {
        o.pause();
        o.currentTime = 0;
        o.play();
        return;
    }
    if (e.key == 'v' || e.key == '3') {
        p.pause();
        p.currentTime = 0;
        p.play();
        return;
    }
    if (e.key == 'b') {
        q.pause();
        q.currentTime = 0;
        q.play();
        return;
    }
    if (e.key == 'n') {
        r.pause();
        r.currentTime = 0;
        r.play();
        return;
    }
    if (e.key == 'j') {
        t.pause();
        t.currentTime = 0;
        t.play();
        return;
    }
    if (e.key == 'k') {
        u.pause();
        u.currentTime = 0;
        u.play()
        return;
    }
    if (e.key == 'm') {
        v.pause();
        v.currentTime = 0;
        v.play();
        return;
    }
    if (e.key == 'o') {
        w.pause();
        w.currentTime = 0;
        w.play();
        return;
    }
    if (e.key == 'p') {
        w2.pause();
        w2.currentTime = 0;
        w2.play()
        return;
    }
    y.pause();
    y.currentTime = 0;
    y.play();
}

function getRandomColor() {
    let letters = '0123456789ABCDEF';
    let color = '#';
    for (let i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}