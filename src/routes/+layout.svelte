<script>
import "../global.css";
import Nav from "../components/Nav.svelte";
import { goto } from '$app/navigation';
import { onMount } from 'svelte';

onMount(() => {
    if (window.location.pathname === '/') {
        goto('/explore/title');
    }
});
</script>

<div class="layout-container">
    <Nav />
    <div class="content">
        <slot></slot>
    </div>
</div>

<style>
.layout-container {
    width: 100%;
    height: 100%;
    padding: 0;
    margin: 0;
    display: flex;
    flex-direction: column;
    box-sizing: border-box;
    background-color: #181A1B;
}

.content {
    flex: 1;
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    box-sizing: border-box;
    font-family: inherit;
}
</style>
