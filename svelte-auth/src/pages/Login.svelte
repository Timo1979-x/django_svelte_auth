<script>
  import axios from "axios";
  import { push } from "svelte-spa-router";
  import { authenticated } from "../store/auth";
  let email = "",
    password = "";
  $: submit = async () => {
    const { data } = await axios.post(
      "login",
      {
        email,
        password,
      },
      { withCredentials: true },
    );

    axios.defaults.headers.common["Authorization"] = `Bearer ${data.token}`;
    authenticated.set(true);

    await push("/");
  };
</script>

<main class="form-signin w-100 m-auto">
  <form on:submit|preventDefault={submit}>
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
    <button class="btn btn-primary w-100 py-2" type="submit">Login</button>
  </form>
</main>
