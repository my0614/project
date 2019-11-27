
        
           document.getElementById('hap').value= localStorage.getItem('total');
           cal =   document.getElementById('hap').value;


           function Comma(cal) {
            return cal.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
         }
         document.getElementById('hap').value = Comma(cal);
         document.getElementById('user').value = localStorage.getItem('username');


         var today = new Date();
var dd = today.getDate();
var mm = today.getMonth()+1; //January is 0!
var yyyy = today.getFullYear();

if(dd<10) {
    dd='0'+dd
} 

if(mm<10) {
    mm='0'+mm
} 

today = yyyy+'년 ' + mm + '월 ' + dd + '일';
document.write(today);

document.getElementById('today').value = today;