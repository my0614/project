
const foods = document.getElementsByClassName("food");
document.getElementById('input').value = localStorage.getItem('total');
for(let i = 0; i < foods.length; i++) {
    foods[i].addEventListener('click', function(){
         choose=confirm("정말로 구매하시겠습니까?");
        if(choose == true)
        {
            console.log(this.name);
            var input = document.getElementById('input');
            input.value =  parseInt(input.value) + parseInt(this.name);

            localStorage.setItem('total',input.value);
            document.getElementById('input').innerHTML = localStorage.getItem('total');

           
        }
       
    })
  
}

function order()
{
   order =  confirm("정말로 주문 하시겠습니까?","");
    if(order ==true)
    {
        window.location.href="order.html";
    }
}
