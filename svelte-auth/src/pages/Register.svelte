<script>
  import axios from "axios";
  import { push } from "svelte-spa-router";
  let first_name = "",
    last_name = "",
    email = "",
    password = "",
    password_confirm = "";
  $: submit = async () => {
    await axios.post("register", {
      first_name,
      last_name,
      email,
      password,
      password_confirm,
    });
    await push("/login");
  };
</script>

<main class="form-signin w-100 m-auto">
  <form on:submit|preventDefault={submit}>
    <h1 class="h3 mb-3 fw-normal">Please register</h1>

    <div class="form-floating">
      <input
        bind:value={first_name}
        class="form-control"
        id="firstName"
        placeholder="First Name"
      />
      <label for="firstName">First Name</label>
    </div>
    <div class="form-floating">
      <input
        bind:value={last_name}
        class="form-control"
        id="lastName"
        placeholder="Last Name"
      />
      <label for="lastName">Last Name</label>
    </div>
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
