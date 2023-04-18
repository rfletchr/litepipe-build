# Lite-Pipe Build Utils

## Icon Builder

Litepipe Icon takes a icon spec file and generates a set of icons from it. This allows the developer to define their
icons in a declarative way. The main benefit of this is that the icons don't need to be checked into the repository and
can be generated at build time. It also removes the need for QtAwesome at runtime.

### Icon Spec

The icon spec file is a YAML file that defines the icons that should be generated.

``` yaml
size: 256 # The size of the icons

icons:
  icons/spanner.png: # the name of an icon
    layers: 
      - fa.square # string layers are assumed to be the name of a QtAwesome icon, and will always be black
      - icon: fa.cog # dict layers can have a name, a color, and a scale_factor
        name: cog
        scale_factor: 0.5       
```

### Usage

``` bash
litepipe-icon icons.yaml --output icons
```

