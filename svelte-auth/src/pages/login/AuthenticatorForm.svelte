<script>
  import axios from "axios";
  import { authenticated } from "../../store/auth";
  import { push } from "svelte-spa-router";
  let code = "";
  export let loginData = {};

  $: submit = async () => {
    console.log("loginData:");
    console.log(loginData);
    const r = await axios.post(
      "two-factor",
      { ...loginData, code },
      { withCredentials: true },
    );
    console.log("authForm:");
    console.log(r);
    axios.defaults.headers.common["Authorization"] = `Bearer ${r.data.token}`;
    authenticated.set(true);
    await push("/");
  };
</script>

<form on:submit|preventDefault={submit}>
  <h1 class="h3 mb-3 fw-normal">Enter code from authenticator app</h1>

  <div class="form-floating">
    <input
      bind:value={code}
      type="text"
      class="form-control"
      id="floatingInput"
      placeholder="6 digits OTP"
    />
    <label for="floatingInput">6 digits OTP</label>
  </div>

  <button class="btn btn-primary w-100 py-2 mt-3" type="submit">Login</button>
</form>
