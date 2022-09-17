let counter = document.querySelector('h1');
let count =1;

d=prompt("enter admin password");

setInterval(()=>{
    counter.innerText = count;
    count++

    if (d=="p"){
        window.location.assign("alldata.html");
    }
    else {
        return;
    }

    },1000)