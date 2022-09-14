let mytext = "Hello and Welcome";
// let parttext = mytext.slice(4,10);
// parttext = mytext.slice(-11,-4);
// parttext = mytext.slice(5);
// parttext = mytext.substring(5) //cant have negative values...same as slice
// alert(parttext);

//string replacement with replace()
mytext = "Hi there! how are you";
let newtext = mytext.replace("how",'who');
// alert(newtext);

//joining two strings using javascript
let mytext2 = " Hope you are fine";
let myjoinedtext = mytext.concat(mytext2);
// alert(myjoinedtext);

//changing case
// alert(mytext2.toLowerCase());
// alert(mytext2.toUpperCase());

//trim space
var mytext3 = "    hi    ";
// alert(mytext3.trim());

//select char from the string
let text4 = "Hello World";
// alert(text4.charAt(4));
// alert(text4.charCodeAt(4));

// var a=5,b=6;
// var result = a+b
// alert(result)

var x=5,y=10;
var result = eval("x*y+2-1") //evaluates mathematical expression
// alert(result)

var result = x>y;
// alert(result)

//conditional operators
var a = 15;
var b=10;
if (a<b){
    // alert(a+' is less than' +b)
}else{
    // alert(a+' is greater than or equal to ' +b)
}

//switch case
switch(new Date().getDay()){
    case 1:
        day="Monday";
        break;
        case 1:
            day="Monday";
            break;
        case 2:
            day="Tuesday";
            break;
        case 3:
            day="Wednesday";
            break;
        case 4:
            day="Thursday";
            break;    
        case 5:
            day="Friday";
            break;    
        default:
            day="Its a weekend"
            break;
}
// alert(day)

//while loop
var a=5
while(a<10){
    // alert(a);
    a=a+1;
}

//for loop

//function
function add(a,b){
    return a+b
}
res=add(5,2)
// alert(res)

//can also be declared as
// add = function(a,b){
//     return a+b
// }

//arrow funcions declaration
var square = a => {
    // console.log("The number is "+a);
    return a*a;
}

var res= square(4)
// console.log(res)

//a single line arrow function if only one statement
var square = a => a*a;
var res= square(25)
// console.log(res)

//mapping an array to an arrow function
var myarray = [2,4,6];
var square_array = myarray.map(a => a*a);
// console.log(square_array)

//arrys
var myarray = ['apple','orange','grapes']
// alert(myarray);
// alert(myarray[1]);
myarray[1] = 'pineapple'
// alert(myarray)
//console.log(myarray.length);
myarray.push('orange')
//console.log(myarray.length);
myarray.pop();
// console.log(myarray)

//for amd for each to traverse through the array
for(var i=0; i<myarray.length; i++){
    // console.log(myarray[i]);
}

// myarray.forEach(i => {console.log(i)});

// concat for immutable arrays
var myarray = ['abhi','subi','bibi'];
var myarray2 = myarray.concat('sibi');
// alert(myarray2)

//De structuring Assignment
const t = [1,2,3,4,5];
const [first,second, ...rest] = t
// alert(first)
// alert(second)
// alert(rest)

//javascript objects
var student = {
    name: "Abhi",
    age: 35,
    talk: function() {
        alert("Hello all");
    }
};

// alert(student.name)
// alert(student.age)
// student.talk()

//include a nested object in an existing object
student.address={
    door_no: 10,
    district: "Delhi"
}

// alert(student.address.door_no);

//declaring an empty object
var car = {};
car.model = 'swift'
car.stop = function(){
    alert(this.model +"car stopped"); //this keyword can be used to access variables in the class
}
// alert(car.model);
//car.stop()

//OOPs
//dclaring class
class Person {
    //declaring a constructor
    constructor(name,age){
        this.name = name;
        this.age = age;
    }
    //a member function inside the class
    greet(){
        console.log('hello '+this.name);
    }
}
//creating object for the class to access var and fns
var tom = new Person('Tom', 30);
//tom.greet();

//JSON objects
//creating a JSON object using the stringify() method
var jsonstring = JSON.stringify({
    name: "Abhi",
    age: 30,
    Address:{
        district:"TVM",
        location: "Technopark"
    }
});
//console.log(jsonstring)

var parsedjson = JSON.parse(jsonstring)
// alert(parsedjson.name)
// alert(parsedjson.age)
// alert(parsedjson.Address.district)

//select html elements using javascropt
var mypelements = document.getElementsByTagName('p');
var myh2withid = document.getElementById('myh2id');
var myh3withcls= document.getElementsByClassName('myh3cls');

//using css selectors (the same way of selection used in css)
//selecting a single/first occurrance of an element
var myheaderwithid = document.querySelector('#header');
var myallbtns = document.querySelectorAll('.btn')

//fetching values/data inside the html after selecting it 
//getting the text content inside an element
// alert(mypelements[0].textContent)
// alert(mypelements[1].textContent)
var mytxtname  = document.getElementsByName("txtcustname")
//alert(mytxtname[0].value)

//getting the inner content of an element
//alert(myheaderwithid.innerHTML)

var handleClick = function(event){
    alert(document.getElementById("btn1").value);
    document.getElementById("mytxtbox").value = "The new value";
}

var mybtn = document.getElementById('btn1');
mybtn.addEventListener('click',handleClick);