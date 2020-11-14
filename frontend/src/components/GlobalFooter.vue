<template>
  <div>
    <!-- Footer -->
    <footer class="page-footer font-small unique-color-dark pt-4">
      <!-- Footer Elements -->
      <div class="footer_area">
        <div class="footer_logo">
          <img src="@/assets/img/car-logo.png">
          <p>Car Select</p>
        </div>
        <!-- Call to action -->
        <ul class="list-unstyled list-inline text-center py-2">
          <li class="list-inline-item back-color-start">
            <a href="#"><v-btn>はじめる</v-btn></a>
          </li>
          <li class="list-inline-item back-color-concept">
            <a href="#"><v-btn>コンセプト</v-btn></a>
          </li>
        </ul>
        <!-- Call to action -->
      </div>
      <!-- Footer Elements -->
      <!-- Copyright -->
      <div class="footer-copyright text-center py-3">© 2020 Copyright:
        <a href="https://mdbootstrap.com/education/bootstrap/"> Ryo's Portfolio</a>
      </div>
      <!-- Copyright -->

    </footer>
    <!-- Footer -->

  </div>
</template>


<script>
export default{

}
</script>



<style lang="scss" scoped>
footer{
  background-color: #1c2331 !important;

  a{
    color: #fff;
  }

  ul li{
    list-style: none;
    display: inline-block;
    margin: 0 10px;
  }

  .back-color-start{
    
    a{
      text-decoration: none;
    }
    
    button{
      background-color: #329eff!important;
      font-size: 0.9rem;
      color: #fff;
      font-weight: bold;
      text-decoration: none;
      outline: none;
    }
  }
  .back-color-concept{
    
    a{
      text-decoration: none;
    }
    
    button{
      background-color: #f5f5f5;
      font-size: 0.9rem;
      color: grey;
      font-weight: bold;
      text-decoration: none;
      outline: none;
    }
  }

}


footer.page-footer button {
  border-radius: 8px;
  width: 147px;
  font-size: 1rem;
  padding: 10px;
}

footer.page-footer button.btn-main {
  background: #329eff;
}

footer.page-footer button.btn-sub {
  background: #565656;
}

footer.page-footer .footer_area {
  margin: 50px auto 80px;
}

footer.page-footer .footer_area .footer_logo {
  text-align: center;
}

footer.page-footer .footer_area .footer_logo img {
  width: 100px;
}

footer.page-footer .footer_area .footer_logo p {
  font-size: 57px;
  font-weight: bold;
  color: #fff;
  letter-spacing: 0.01em;
  font-family: Noto Sans JP;
}

footer.page-footer .footer_area .footer_logo ul {
  margin-bottom: 70px !important;
}

footer .footer-copyright {
  border-top: solid 2px rgba(255, 255, 255, 0.2);
  overflow: hidden;
  color: rgba(255,255,255,0.6);
  background-color: rgba(0,0,0,0.2);
}

#app{
  button{
    padding: 25px;
  }

  height: 500px;
}
</style>