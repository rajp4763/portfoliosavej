function bton() {
    var inp = document.querySelectorAll('input');
    for (let index = 0; index < inp.length; index++) {
        const element = inp[index];
        if (element.value != '') {
            document.getElementById("submit").setAttribute("disabled", "True");
        } else {
            document.getElementById("submit").setAttribute("disabled", "True");
        }
    }
}

var b1 = document.getElementById('ome');
var b2 = document.getElementById('bout');
var b3 = document.getElementById('ervice');
var b4 = document.getElementById('ontact');
var b5 = document.getElementById('ork');
b1.addEventListener("click",function(){
	b1.style.color = 'white'
	b2.style.color = 'grey'
	b3.style.color = 'grey'
	b4.style.color = 'grey'
	b5.style.color = 'grey'

})
b2.addEventListener("click",function(){
	b1.style.color = 'grey'
	b2.style.color = 'white'
	b3.style.color = 'grey'
	b4.style.color = 'grey'
	b5.style.color = 'grey'
})
b3.addEventListener("click",function(){
	b1.style.color = 'grey'
	b2.style.color = 'grey'
	b3.style.color = 'white'
	b4.style.color = 'grey'
	b5.style.color = 'grey'
})
b4.addEventListener("click",function(){
	b1.style.color = 'grey'
	b2.style.color = 'grey'
	b3.style.color = 'grey'
	b4.style.color = 'white'
	b5.style.color = 'grey'
})
b5.addEventListener("click",function(){
	b1.style.color = 'grey'
	b2.style.color = 'grey'
	b3.style.color = 'grey'
	b4.style.color = 'grey'
	b5.style.color = 'white'
})
