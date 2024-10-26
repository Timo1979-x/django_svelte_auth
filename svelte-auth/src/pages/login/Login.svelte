<script>
  import AuthenticatorForm from "./AuthenticatorForm.svelte";
  import LoginForm from "./LoginForm.svelte";
  import qrcode from "qrcode";

  let loginData = {
    id: 0,
  };
  let src = "";

  $: login = (event) => {
    // console.log(event);
    loginData = event.detail;
    if (loginData.otpauth_url) {
      qrcode.toDataURL(loginData.otpauth_url, (err, data) => {
        src = data;
      });
    }
  };
</script>

<main class="form-signin w-100 m-auto">
  {#if loginData.id === 0}
    <LoginForm on:login={login} />
  {:else}
    <AuthenticatorForm {loginData} />
    {#if src !== ""}
      <img {src} alt="" class="w-100"/>
    {/if}
  {/if}
</main>
