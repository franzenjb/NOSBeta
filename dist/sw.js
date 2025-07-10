// Service Worker for Performance Optimization
const CACHE_NAME = 'nosb-v1.0.0';
const CACHE_DURATION = 5 * 60 * 1000; // 5 minutes

// Assets to cache immediately
const STATIC_ASSETS = [
    '/',
    '/index_optimized.html',
    '/styles.css',
    '/manifest.json'
];

// API endpoints to cache with network-first strategy
const API_ENDPOINTS = [
    'https://menu-jfranzen.pythonanywhere.com/menu'
];

// Install event - cache static assets
self.addEventListener('install', event => {
    console.log('Service Worker installing...');
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then(cache => {
                console.log('Caching static assets');
                return cache.addAll(STATIC_ASSETS);
            })
            .then(() => {
                console.log('Static assets cached');
                return self.skipWaiting();
            })
    );
});

// Activate event - clean up old caches
self.addEventListener('activate', event => {
    console.log('Service Worker activating...');
    event.waitUntil(
        caches.keys().then(cacheNames => {
            return Promise.all(
                cacheNames
                    .filter(cacheName => cacheName !== CACHE_NAME)
                    .map(cacheName => {
                        console.log('Deleting old cache:', cacheName);
                        return caches.delete(cacheName);
                    })
            );
        }).then(() => {
            console.log('Service Worker activated');
            return self.clients.claim();
        })
    );
});

// Fetch event - implement caching strategies
self.addEventListener('fetch', event => {
    const request = event.request;
    const url = new URL(request.url);

    // Skip non-GET requests
    if (request.method !== 'GET') {
        return;
    }

    // API requests - network first with cache fallback
    if (API_ENDPOINTS.some(endpoint => request.url.includes(endpoint))) {
        event.respondWith(networkFirstStrategy(request));
    }
    // Static assets - cache first
    else if (STATIC_ASSETS.includes(url.pathname)) {
        event.respondWith(cacheFirstStrategy(request));
    }
    // Other requests - stale while revalidate
    else {
        event.respondWith(staleWhileRevalidateStrategy(request));
    }
});

// Network-first strategy for API calls
async function networkFirstStrategy(request) {
    const cacheName = CACHE_NAME;
    
    try {
        // Try network first
        const networkResponse = await fetch(request);
        
        if (networkResponse.ok) {
            // Cache successful response
            const cache = await caches.open(cacheName);
            cache.put(request, networkResponse.clone());
            return networkResponse;
        }
        
        throw new Error('Network response not ok');
    } catch (error) {
        console.log('Network failed, trying cache for:', request.url);
        
        // Fallback to cache
        const cachedResponse = await caches.match(request);
        if (cachedResponse) {
            return cachedResponse;
        }
        
        // Return offline fallback for API requests
        return new Response(
            JSON.stringify({ 
                categories: [],
                error: 'Offline - cached data not available'
            }), 
            {
                status: 200,
                headers: { 'Content-Type': 'application/json' }
            }
        );
    }
}

// Cache-first strategy for static assets
async function cacheFirstStrategy(request) {
    const cachedResponse = await caches.match(request);
    
    if (cachedResponse) {
        return cachedResponse;
    }
    
    try {
        const networkResponse = await fetch(request);
        
        if (networkResponse.ok) {
            const cache = await caches.open(CACHE_NAME);
            cache.put(request, networkResponse.clone());
        }
        
        return networkResponse;
    } catch (error) {
        console.error('Failed to fetch:', request.url, error);
        throw error;
    }
}

// Stale-while-revalidate strategy for other resources
async function staleWhileRevalidateStrategy(request) {
    const cache = await caches.open(CACHE_NAME);
    const cachedResponse = await cache.match(request);
    
    // Fetch in background to update cache
    const fetchPromise = fetch(request).then(networkResponse => {
        if (networkResponse.ok) {
            cache.put(request, networkResponse.clone());
        }
        return networkResponse;
    }).catch(error => {
        console.log('Background fetch failed:', error);
    });
    
    // Return cached version immediately, or wait for network
    return cachedResponse || fetchPromise;
}

// Background sync for offline actions
self.addEventListener('sync', event => {
    if (event.tag === 'background-sync') {
        event.waitUntil(doBackgroundSync());
    }
});

async function doBackgroundSync() {
    console.log('Background sync triggered');
    // Implement background sync logic here
    // For example, sync any offline actions when connection is restored
}

// Message handling from main thread
self.addEventListener('message', event => {
    if (event.data && event.data.type === 'SKIP_WAITING') {
        self.skipWaiting();
    }
    
    if (event.data && event.data.type === 'CACHE_URLS') {
        event.waitUntil(
            caches.open(CACHE_NAME).then(cache => {
                return cache.addAll(event.data.payload);
            })
        );
    }
});

// Performance monitoring
self.addEventListener('fetch', event => {
    const start = performance.now();
    
    event.respondWith(
        (async () => {
            const response = await handleRequest(event.request);
            const duration = performance.now() - start;
            
            // Log performance metrics (could send to analytics)
            console.log(`Request to ${event.request.url} took ${duration.toFixed(2)}ms`);
            
            return response;
        })()
    );
});

async function handleRequest(request) {
    // Use appropriate strategy based on request type
    // This is a simplified version - the actual logic is in the main fetch listener
    return fetch(request);
}