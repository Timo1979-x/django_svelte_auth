<script>
  import axios from "axios";
  import { onMount } from "svelte";
  let message = "You are not logged in";

  onMount(async () => {
    const { data } = await axios.get("user");
    message = `Hi ${data.first_name} ${data.last_name}`;
  });
</script>

<div class="container mt-5 text-center">
  <h3>{message}</h3>
</div>
