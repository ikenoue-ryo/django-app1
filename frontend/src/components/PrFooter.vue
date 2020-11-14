<template>
    <div class="pr_footer">
      <!-- Copyright -->
      <div class="footer-copyright text-center py-3">© 2020 Copyright:
        <a href="https://mdbootstrap.com/education/bootstrap/"> Ryo's Portfolio</a>
      </div>
      <!-- Copyright -->
    </div>
</template>


<script>
export default{

}
</script>



<style lang="scss" scoped>
.pr_footer{
  background-color: #1c2331;

  .text-center{
    text-align: center;
  }
}

.footer-copyright{
  border-top: solid 2px rgba(255, 255, 255, 0.2);
  overflow: hidden;
  color: rgba(255, 255, 255, 0.6);
  background-color: rgba(0, 0, 0, 0.2);
  padding: 10px;

  a{
    color: #fff;
  }
}
</style>