<template>
  <div class="min-h-screen bg-secondary-200 font-sans">
    <div class="bg-primary-600 pb-32">
      <Disclosure as="nav" class="bg-primary-600 border-b border-primary-300 border-opacity-25 lg:border-none" v-slot="{ open }">
        <div class="max-w-7xl mx-auto px-2 sm:px-4 lg:px-8">
          <div class="relative h-16 flex items-center justify-between lg:border-b lg:border-primary-400 lg:border-opacity-25">
            <div class="px-2 flex items-center lg:px-0">
              <div class="flex-shrink-0">
                <div class="text-secondary-50 flex items-center justify-left cursor-default">
                  <logo class="h-8 w-8" alt="Django Guides Code Sample" />
                  <span class="hidden lg:inline ml-3 text-xl font-bold font-brand">Django Guides Code Sample</span>
                </div>
              </div>
              <div class="hidden lg:block lg:ml-10">
                <div class="flex space-x-4">
                  <template v-for="item in navItems" :key="item">
                    <template v-if="!!item.current">
                      <router-link :to="item.href" class="bg-primary-700 text-secondary-50 rounded-md py-2 px-3 text-sm font-medium cursor-default">
                        {{ item.name }}
                      </router-link>
                    </template>
                    <router-link v-else :to="item.href" class="text-secondary-50 hover:bg-primary-500 hover:bg-opacity-75 rounded-md py-2 px-3 text-sm font-medium">
                      {{ item.name }}
                    </router-link>
                  </template>
                </div>
              </div>
            </div>
            <div class="flex-1 px-2 flex justify-center lg:ml-6 lg:justify-end">
              <div class="max-w-lg w-full lg:max-w-xs">
                <label for="search" class="sr-only">Search</label>
                <div class="relative text-secondary-400 focus-within:text-secondary-600">
                  <div class="pointer-events-none absolute inset-y-0 left-0 pl-3 flex items-center">
                    <SearchIcon class="h-5 w-5" aria-hidden="true" />
                  </div>
                  <input id="search" class="block w-full bg-secondary-50 py-2 pl-10 pr-3 border border-transparent rounded-md leading-5 text-secondary-900 placeholder-secondary-500 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-primary-600 focus:ring-secondary-50 focus:border-secondary-50 sm:text-sm" placeholder="Search" type="search" name="search" />
                </div>
              </div>
            </div>
            <div class="flex lg:hidden">
              <!-- Mobile menu button -->
              <DisclosureButton class="bg-primary-600 p-2 rounded-md inline-flex items-center justify-center text-primary-200 hover:text-secondary-50 hover:bg-primary-500 hover:bg-opacity-75 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-primary-600 focus:ring-secondary-50">
                <span class="sr-only">Open main menu</span>
                <MenuIcon v-if="!open" class="block h-6 w-6" aria-hidden="true" />
                <XIcon v-else class="block h-6 w-6" aria-hidden="true" />
              </DisclosureButton>
            </div>
            <div class="hidden lg:block lg:ml-4">
              <div class="flex items-center">
                <span class="text-secondary-50 font-bold">{{ welcomeText }}</span>

                <!-- Profile dropdown -->
                <Menu as="div" class="ml-3 relative flex-shrink-0">
                  <div>
                    <MenuButton class="bg-primary-600 rounded-full flex text-sm text-secondary-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-primary-600 focus:ring-secondary-50">
                      <span class="sr-only">Open user menu</span>
                      <profile-picture class="h-8 w-8 img-rounded" :user="auth?.user" />
                    </MenuButton>
                  </div>
                  <transition enter-active-class="transition ease-out duration-100" enter-from-class="transform opacity-0 scale-95" enter-to-class="transform opacity-100 scale-100" leave-active-class="transition ease-in duration-75" leave-from-class="transform opacity-100 scale-100" leave-to-class="transform opacity-0 scale-95">
                    <MenuItems class="origin-top-right absolute right-0 mt-2 w-48 rounded-md shadow-lg py-1 bg-secondary-50 ring-1 ring-secondary-900 ring-opacity-5 focus:outline-none">
                      <MenuItem v-for="item in profileItems" :key="item" v-slot="{ active }">
                        <router-link :to="item.href" :class="[active ? 'bg-secondary-100' : '', 'block py-2 px-4 text-sm text-secondary-700']">
                          {{ item.name }}
                        </router-link>
                      </MenuItem>
                      <MenuItem v-slot="{ active }" v-if="!!auth?.user">
                        <a href="#" :class="[active ? 'bg-secondary-100' : '', 'block py-2 px-4 text-sm text-secondary-700']" @click.prevent="onLogout">
                          Sign Out
                        </a>
                      </MenuItem>
                    </MenuItems>
                  </transition>
                </Menu>
              </div>
            </div>
          </div>
        </div>

        <DisclosurePanel class="lg:hidden">
          <div class="px-2 pt-2 pb-3 space-y-1">
            <template v-for="item in navItems" :key="item">
              <template v-if="!!item.current">
                <router-link :to="item.href" class="bg-primary-700 text-secondary-50 block rounded-md py-2 px-3 text-base font-medium">
                  {{ item.name }}
                </router-link>
              </template>
              <router-link v-else :to="item.href" class="text-secondary-50 hover:bg-primary-500 hover:bg-opacity-75 block rounded-md py-2 px-3 text-base font-medium">
                {{ item.name }}
              </router-link>
            </template>
          </div>
          <div class="pt-4 pb-3 border-t border-primary-700">
            <div class="px-5 flex items-center">
              <div class="flex-shrink-0 text-secondary-50">
                <profile-picture class="h-10 w-10" :user="user" />
              </div>
              <div class="ml-3">
                <div class="text-base font-medium text-secondary-50">{{ fullName }}</div>
                <div class="text-sm font-medium text-primary-300">{{ username }}</div>
              </div>
            </div>
            <div class="mt-3 px-2 space-y-1">
              <router-link v-for="item in profileItems" :key="item" :to="item.href" class="block rounded-md py-2 px-3 text-base font-medium text-secondary-50 hover:bg-primary-500 hover:bg-opacity-75">
                {{ item.name }}
              </router-link>
              <a href="#" class="block rounded-md py-2 px-3 text-base font-medium text-secondary-50 hover:bg-primary-500 hover:bg-opacity-75" @click.prevent="onLogout" v-if="!!auth?.user">
                Sign Out
              </a>
            </div>
          </div>
        </DisclosurePanel>
      </Disclosure>
      <header class="py-10">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <h1 class="text-3xl font-bold text-secondary-50">
            <slot name="title" />
          </h1>
        </div>
      </header>
    </div>

    <main class="-mt-32">
      <div class="max-w-7xl mx-auto pb-12 px-4 sm:px-6 lg:px-8">
        <div class="bg-secondary-50 rounded-lg shadow px-5 py-6 sm:px-6">
          <Banner v-if="flashMessage">
            {{ flashMessage }}
          </Banner>
          <slot />
        </div>
      </div>
    </main>

    <page-footer />
  </div>
</template>

<script>
import { Disclosure, DisclosureButton, DisclosurePanel, Menu, MenuButton, MenuItem, MenuItems } from '@headlessui/vue'
import { SearchIcon } from '@heroicons/vue/solid'
import { MenuIcon, XIcon } from '@heroicons/vue/outline'

import FlashMessage from '@/utils/FlashMessage'
import LazyAxiosRequest from '@/utils/LazyAxiosRequest'
import Logo from '@/components/Logo'
import MakeNavigation from '@/utils/MakeNavigation'
import MakeProfileNavigation from '@/utils/MakeProfileNavigation'
import Banner from '@/components/Banner'
import ProfilePicture from '@/components/auth/ProfilePicture'
import PageFooter from '@/components/site-pages/PageFooter'

/**
 * The main Layout for site pages. Includes the header, footer, and styles.
 */
export default {
  name: 'PageLayout',

  components: {
    Banner,
    Disclosure,
    DisclosureButton,
    DisclosurePanel,
    Logo,
    Menu,
    MenuButton,
    MenuIcon,
    MenuItem,
    MenuItems,
    PageFooter,
    ProfilePicture,
    SearchIcon,
    XIcon
  },

  inject: ['auth'],

  data () {
    return {
      // Flash Message (usually from the previous page)
      flashMessage: FlashMessage.getFlashMessage(),

      // Is the Menu open? (Up to Medium screen size)
      open: false
    }
  },

  computed: {
    // User's full name
    fullName () {
      let fullName = 'Guest'
      // noinspection JSUnresolvedVariable
      if (this.auth?.user?.first_name) {
        if (this.auth?.user?.last_name) {
          fullName = this.auth?.user.first_name + ' ' + this.auth?.user.last_name
        } else {
          fullName = this.auth?.user.first_name
        }
      } else if (this.auth?.user?.username) {
        fullName = ''
      }
      return fullName
    },

    // User's username
    username () {
      // noinspection JSUnresolvedVariable
      return this.auth?.user?.username ?? ''
    },

    // Text to display as a "welcome" message
    welcomeText () {
      // noinspection JSUnresolvedVariable
      if (!this.auth?.user) {
        return 'Guest'
      }
      if (this.auth?.user?.first_name) {
        return 'Welcome, ' + this.auth?.user?.first_name
      }
      if (this.auth?.user?.username) {
        return 'Welcome, ' + this.auth?.user?.username
      }
      return 'Welcome!'
    },

    profileItems () {
      return MakeProfileNavigation(this.auth?.user)
    },

    navItems () {
      return MakeNavigation(this.auth?.user)
    }
  },

  methods: {
    // Process a logout request
    onLogout () {
      LazyAxiosRequest('/api/auth/logout/', {})
        .then(function () {
          FlashMessage.setFlashMessage('You have been logged out.')
        })
        .catch(function (error) {
          console.error('Logout Error: ', error)
        })
        .finally(function () {
          if (this.auth && this.auth.logout) {
            this.auth.logout()
            this.$router.go()
          }
        }.bind(this))
    }
  }
}
</script>
