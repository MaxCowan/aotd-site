<script>
import { goto } from '$app/navigation';
import { onMount } from 'svelte';

onMount(() => {
    if (window.location.pathname === '/explore') {
        goto('/explore/title');
    }
});
</script>

<slot />
