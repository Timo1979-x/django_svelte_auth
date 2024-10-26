<script>
  import axios from "axios";
  import { push } from "svelte-spa-router";
  let password = "",
    password_confirm = "";

  export let params;
  $: submit = async () => {
    console.log(`reset token is ${params.token}`);
    await axios.post("reset", {
      token: params.token,
      password,
      password_confirm,
    });
    await push("/login");
  };
</script>

<main class="form-signin w-100 m-auto">
  <form on:submit|preventDefault={submit}>
    <h1 class="h3 mb-3 fw-normal">Reset password</h1>

    <div class="form-floating">
      <input
        bind:value={password}
        type="password"
        class="form-control"
        id="floatingPassword1"
        placeholder="Password"
      />
      <label for="floatingPassword1">Password</label>
    </div>
    <div class="form-floating">
      <input
        bind:value={password_confirm}
        type="password"
        class="form-control"
        id="floatingPassword2"
        placeholder="Password confirmation"
      />
      <label for="floatingPassword2">Password confirmation</label>
    </div>

    <button class="btn btn-primary w-100 py-2" type="submit">Submit</button>
  </form>
</main>
