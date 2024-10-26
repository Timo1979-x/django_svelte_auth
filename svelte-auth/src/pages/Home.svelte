<script>
  import axios from "axios";
  import { onMount } from "svelte";
    import { authenticated } from "../store/auth";
  let message = "You are not logged in!";

  onMount(async () => {
    const response = await axios.get("user");
    console.log(`Home.onMount response:`);
    console.log(response);
    let status = response.status;
    let data = response.data;
    if(status === 200) {
      message = `Hi ${data.first_name} ${data.last_name}`;
      authenticated.set(true);
    } else {
      message = "You are not logged in!";
      authenticated.set(false);
    }
  });
</script>

<div class="container mt-5 text-center">
  <h3>{message}</h3>
</div>
