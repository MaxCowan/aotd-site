import { writable } from 'svelte/store';

export const albums = writable([]);
let loaded = false;

export const fetchSheetAlbums = async () => {
	// TODO verify that we're not making requests on refresh. 
    // I guess this means if there's new content in the sheet, it can only be viewed in a new window.
    if (loaded) return;
	const url = `https://opensheet.elk.sh/1BHiz9vy3RSPuIenqPnC_HFlvT0scBxh2dCogildeVm0/1:%20Album%20of%20the%20Day`;
	const res = await fetch(url);
	const data = await res.json();
	const loadedAlbums = data.map((data, index) => ({
		albumName: data.Album
	}));

    // TODO remove excessive logging
    console.log(loadedAlbums); 
	albums.set(loadedAlbums);
    loaded = true;
};
