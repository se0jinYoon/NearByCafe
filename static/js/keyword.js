// function loadKeyword(){
//     var xmlhttp = new XMLHttpRequest();

//     xmlhttp.onreadystatechange = function() {
//         if(xmlhttp.readyState == XMLHttpRequest.DONE){
//             if(xmlhttp.status == 200){
//                 document.getElementsByClassName('keyword_list').innerHtml = xmlhttp.response;
//             }
//             else if(xmlhttp.status == 400){
//                 alert("400 error");
//             }
//             else{
//                 alert("somthing wrong");
//             }
//         }
//     }
// };
var state = 0;
const onClickKeywordList = async() => {

  var keyword_list = await fetch( "/cafe/keyword_list/").then(console.log(Response))
//   keyword_list = ["공부하기 좋은"];
keyword_list=[
    '데이트',
    '작업하기 좋은',
    '공부하기 좋은',
    '조용한',
    '시끌벅적한',
    '의자가 편한',
    '디저트 맛있는',
    '커피가 맛있는',
    '친절한',
    '혼카페',
    '장소가 넓은',
    '콘센트가 많은',
    '화장실 깨끗한',
    '인테리어 예쁜',  
    ]
if(state === 0){
  keywordHandleResponse(keyword_list);}
  else{
    var element = document.querySelector(".keyword_list");
    element.innerHTML = ``;
    state = 0;
  }
}
const keywordHandleResponse = (keyword_list) =>{
    var element = document.querySelector(".keyword_list");
    state = 1;
    // element.innerHTML = `${keyword_list}`;
    element.innerHTML = `<h3>검색할 키워드를 선택해주세요.</h3></br>`;
    originHTML = element.innerHTML;
   keyword_list.forEach(item => {
    element.innerHTML += ` <a href="" style="text-decoration: none; color : black;">${item}</a> </br>`
   });
}

// location list 가져오기
const requestLocation=new XMLHttpRequest();
// const onClickLocation=async()=>{
//     const url="/keyword_location";
//     const {data}=await axios.post(url,{
//     });
//     locationHandleResopnse(data.location);
    
// };

const onClickShowLocationList=()=>{
    const url='/keywords_location';
    var table=document.querySelector(`location modal`).value;
    requestLocation.open('POST',url,true)
    requestLocation.setRequestHeader(
        "Content-Type",
        "application/x-www-form-urlencoded"
    );
    requestLocation.send(JSON.string)

}

    

