<script>
  import Home from "./pages/Home.svelte";
  import Login from "./pages/Login.svelte";
  import Register from "./pages/Register.svelte";
  import Router from "svelte-spa-router";
  import Forgot from "./pages/Forgot.svelte";
  import Nav from "./components/Nav.svelte";

  const routes = {
    "/": Home,
    "/login": Login,
    "/register": Register,
    "/forgot": Forgot,
  };
</script>

<Nav />

<Router {routes} />
