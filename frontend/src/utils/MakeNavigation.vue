<script>
import { HomeIcon,
  // ViewListIcon
} from '@heroicons/vue/solid'

export default function (user) {
  const navItems = []
  const authenticated = (!!user)

  navItems.push({ name: 'Home', href: '/', icon: HomeIcon, current: true })
  // navItems.push({ name: 'Games', href: '/games', icon: ViewListIcon, current: false })
  if (authenticated) {
    // navItems.push({ name: 'Guides', href: '/guides', icon: ViewListIcon, current: false })
    // navItems.push({ name: 'Playthroughs', href: '/playthroughs', icon: ViewListIcon, current: false })
  }
  return navItems
}
</script>
