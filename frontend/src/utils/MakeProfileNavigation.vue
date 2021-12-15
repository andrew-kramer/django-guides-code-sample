<script>
import {
  // CogIcon,
  LoginIcon,
  UserAddIcon,
  // UserIcon
} from '@heroicons/vue/solid'

export default function (user) {
  const navItems = []
  const authenticated = (!!user)

  if (authenticated) {
    // navItems.push({ name: 'Profile', href: '#', icon: UserIcon, current: false })
    // navItems.push({ name: 'Settings', href: '#', icon: CogIcon, current: false })
  } else {
    navItems.push({ name: 'Sign In', href: '/login', icon: LoginIcon, current: false })
    navItems.push({ name: 'Sign Up', href: '/register', icon: UserAddIcon, current: false })
  }
  return navItems
}
</script>
