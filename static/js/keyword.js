
////////////////// KEYWORD 가져오기 ////////////
var keyword_state = 0; 
const onClickKeywordList = async() => {

  var keyword_list = await fetch( "/cafe/keyword_list/").then(console.log(Response))

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
if(keyword_state === 0){
  keywordHandleResponse(keyword_list);}
  else{
    var element = document.querySelector(".keyword_list");
    element.innerHTML = ``;
    keyword_state = 0;
  }
}
const keywordHandleResponse = (keyword_list) =>{
    var element = document.querySelector(".keyword_list");
    keyword_state = 1;
    // element.innerHTML = `${keyword_list}`;
    element.innerHTML = `<h3>검색할 키워드를 선택해주세요.</h3></br>`;
    originHTML = element.innerHTML;
   keyword_list.forEach(item => {
    element.innerHTML += ` <a href="" style="text-decoration: none; color : black;">${item}</a> </br>`
   });
}

//////////////// location list 가져오기
var location_state=0;
const onClickLocationList=async()=>{
  var location_list=await fetch("/cafe/location_list/").then(console.log(Response))
  location_list=[
    '서울 전체',
     '왕십리/한양대/성수',
     '강남/역삼/선릉/압구정',
     '건대입구/세종대',
     '서울대입구/신림',
     '동작/흑석/상도',
     '노량진/여의도/영등포/당산',
     '구로/신도림',
     '목동/양천/금천',
     '광운대/공릉/노원/도봉',
     '수유/미아',
     '김포공항/염창/강서',
     '홍대/합정/망원/서강',
     '신촌/이대/서대문/아현',
     '혜화/성균관대',
     '청량리/회기',
     '성신여대/안암/성북/길음',
     '잠실/송파/강동',
     '을지로/명동/중구',
     '서초/교대/사당',
     '종로/인사동/동대문',
     '서울역/이태원/용산',
     '중랑/쌍봉',
     ]

     if(location_state === 0){
      locationHandleResponse(location_list);}
      else{
        var element = document.querySelector(".location_list");
        element.innerHTML = ``;
        location_state = 0;
      }
    }

    const locationHandleResponse = (location_list) =>{
      var element = document.querySelector(".location_list");
      location_state = 1;
      // element.innerHTML = `${keyword_list}`;
      element.innerHTML = `<h3>검색할 위치를 선택해주세요.</h3></br>`;
      originHTML = element.innerHTML;
      location_list.forEach(item => {
      element.innerHTML += ` <a href="" style="text-decoration: none; color : black;">${item}</a> </br>`
     });
  }
