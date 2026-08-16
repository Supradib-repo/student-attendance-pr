let listcontain=document.getElementById("Attendancelist")

fetch("/get")

    .then(response=> response.json())
    .then (lst=>{
        let present=0;
        let absent=0;
        console.log(lst)
        lst.forEach(student => {

            let li =document.createElement("li")
            li.textContent=student.name+"|"+student.departement+"|"+student.date+"|"+student.roll+"|"+student.status

            listcontain.appendChild(li)
            if (student.status=="present"){
                present++; 
             
    }
    else{
        absent++;
    }
});
let total=lst.length;
console.log(present)
console.log(absent)

document.getElementById("present").textContent=present
document.getElementById("absent").textContent=absent
document.getElementById("total").textContent=total

    });