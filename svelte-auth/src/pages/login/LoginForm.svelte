<script>
  import axios from "axios";
  import { link } from "svelte-spa-router";
  import { createEventDispatcher } from "svelte";
  import { GoogleAuth } from "@beyonk/svelte-social-auth";
  import { authenticated } from "../../store/auth";

  let email = "",
    password = "";

  const dispatch = createEventDispatcher();
  $: submit = async () => {
    const { data } = await axios.post("login", { email, password });
    dispatch("login", data);
  };
  $: googleAuth = async (event) => {
    const { status, data } = await axios.post(
      "google-auth",
      {
        token: event.detail.user.wc.id_token,
      },
      { withCredentials: true },
    );

    if (status === 200) {
      axios.defaults.headers.common["Authorization"] = `Bearer ${data.token}`;
      authenticated.set(true);
      await push("/");
    }
  };
</script>

<form on:submit|preventDefault={submit} class="mb-3">
  <h1 class="h3 mb-3 fw-normal">Please sign in</h1>

  <div class="form-floating">
    <input
      bind:value={email}
      type="email"
      class="form-control"
      id="floatingInput"
      placeholder="name@example.com"
    />
    <label for="floatingInput">Email address</label>
  </div>
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

  <div class="mb-3"><a href="/forgot" use:link>Forgot your password?</a></div>
  <button class="btn btn-primary w-100 py-2" type="submit">Login</button>
</form>

<GoogleAuth
  clientId="351723739104-k58pidskm36d2c8ggkgs3vlgv47siqpf.apps.googleusercontent.com"
  on:auth-success={googleAuth}
/>
