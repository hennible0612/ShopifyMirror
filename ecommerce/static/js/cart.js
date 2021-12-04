

var updateBtns = document.getElementsByClassName('update-cart')

for (i = 0; i < updateBtns.length; i++) {
	updateBtns[i].addEventListener('click', function(){
		var productId = this.dataset.product
		var action = this.dataset.action
		console.log('productId:', productId, 'Action:', action)

	})
}
// var updateBtns = document.getElementsByClassName('update-cart')//클래스 이름으로 찾고 updateBtns에 저장
//
// for (i = 0; i < updateBtns.length; i++) { //for문을 돌리는 이유는 모든 updateBtns에게 기능을 추가하기 위함이다.
// 	updateBtns[i].addEventListener('click', function(){ //클릭시 function 실행
// 		var productId = this.dataset.product //커스텀 attribute를 통해 데이터를 가져옴 즉, store.html에 있는 product.id가져옴
// 		var action = this.dataset.action // add가져옴 this는 클릭이 된애
// 		console.log('productId:', productId, 'Action:', action)
//
//     })
// }

