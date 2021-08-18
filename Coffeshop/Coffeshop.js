var menuPrice;
$(document)
    .on('click','#late',function(){
        $('#menuname').val("카페라떼");
        menuPrice=3000;
        return false;
    })
    .on('click','#espresso',function(){
        $('#menuname').val("에스프레소");
        menuPrice=2000;
        return false;
    })
    .on('click','#americano',function(){
        $('#menuname').val("아메리카노");
        menuPrice=2500;
        return false;
    })
    .on('click','#cafuchino',function(){
        $('#menuname').val("카푸치노");
        menuPrice=3500;
        return false;
    })
    .on('blur','#cnt',function(){
        totalPrice = menuPrice*parseInt($('#cnt').val());
        $('#sum').val(totalPrice);
        return false;
    })
    .on('click','#btnadd',function(){
        $('#orderlist').append('<option>'+$('#menuname').val()+' '+$('#cnt').val()+'잔'+' '+$('#sum').val()+'원 </option>')
        return false;
    })
    .on('click','#btndelete',function(){
        if(confirm('삭제하시겠습니까?')){
            $('#orderlist').find('option:last').remove();
        }
        return false;
    })
    .on('click','#btnorder',function(){
        let inMobile = prompt('주문자 모바일 번호');
        $('#Saleslist').append('<option>'+inMobile+' '+$('#menuname').val()+' '+$('#cnt').val()+'잔</option>')
        return false;
    })