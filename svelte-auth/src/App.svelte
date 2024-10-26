<script>
  import Home from "./pages/Home.svelte";
  import Login from "./pages/Login.svelte";
  import Register from "./pages/Register.svelte";
  import Router, { link } from "svelte-spa-router";
  import { onMount } from "svelte";
  import axios from "axios";

  const routes = {
    "/": Home,
    "/login": Login,
    "/register": Register,
  };

  let auth = false;
  
  onMount(async () => {
    try {
      let response = await axios.get("user");
      auth = true;
      console.log(`App.onMount: got user ${response}, auth=${auth}`);
    } catch(e) {
      auth = false;
      console.log(`App.onMount: get user unsuccess ${e}, auth=${auth}`);
    }
  });

  $: logout = async () => {
    axios.post('logout', {}, { withCredentials: true });
    auth = false;
  }
</script>

<header class="p-3 text-bg-dark">
  <div class="container">
    <div
      class="d-flex flex-wrap align-items-center justify-content-center justify-content-lg-start"
    >
      <ul
        class="nav col-12 col-lg-auto me-lg-auto mb-2 justify-content-center mb-md-0"
      >
        <li><a href="/" use:link class="nav-link px-2 text-white">Home</a></li>
      </ul>

      {#if auth}
        <div class="text-end">
          <a href="/login" use:link class="btn btn-outline-light me-2" on:click={logout}>Logout</a>
        </div>
      {:else}
        <div class="text-end">
          <a href="/login" use:link class="btn btn-outline-light me-2">Login</a>
          <a href="/register" use:link class="btn btn-outline-light me-2"
            >Register</a
          >
        </div>
      {/if}
    </div>
  </div>
</header>

<Router {routes} />
