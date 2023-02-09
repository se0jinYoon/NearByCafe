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
const onClickKeywordList = async() => {
    const url = "/cafe/keyword_list/";
    const res = await fetch(url, {
        method : "POST",
        headers : {
            "Content-Type" : "application/x-www-from-urlencoder",
        },
    });
    const keyword_list = await res.json();
    keywordHandleResponse(keyword_list);
};
const keywordHandleResponse = (keyword_list) =>{
    const element = document.querySelector(`.keyword_list`);
    element.innerHTML = `success ${keyword_list}`;
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

    

