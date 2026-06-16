---
title: "2026-06-16_unknown_生成式UI四条演进主线"
source: "omnisun://digest/1774516500816"
author:
  - "[[@openuidev]]"
published: 2026-06-16
created: 2026-06-16
description:
tags:
  - "#371"
  - "#337"
  - "@openuidev"
  - "email"
---

# 生成式UI四条演进主线

# thesysdev/openui: The Open Standard for Generative UI

https://github.com/thesysdev/openui

[Open in github.dev](https://github.dev/) [Open in a new github.dev tab](https://github.dev/) [Open in codespace](/codespaces/new/thesysdev/openui?resume=1)

| Name | Name | 
Last commit message

 | 

Last commit date

 |
| --- | --- | --- | --- |
| 

[bca62da](/thesysdev/openui/commit/bca62da322f2abffbaf86431af35c1a464c1d01e) ·

[444 Commits](/thesysdev/openui/commits/main/)

 |
| 

[.cursor](/thesysdev/openui/tree/main/.cursor ".cursor")

 | 

[.cursor](/thesysdev/openui/tree/main/.cursor ".cursor")

 | 

[Migrate to openui](/thesysdev/openui/commit/3dd7669b8e6a86b627ded9a30447bc601b81af11 "Migrate to openui
This commit migrates the project to openui and replaces existing thesysdev/crayon
with a new Language Specification (@openuidev/openui-lang), React Runtime (@openuidev/lang-react)
alongwith new Headless Chat Runtime (@openuidev/react-headless) plus a DS (@openuidev/react-ui)
Co-authored-by: Abhishek <abhishek@thesys.dev>
Co-authored-by: Aditya <aditya@thesys.dev>
Co-authored-by: Ankit <ankit@thesys.dev>
Co-authored-by: Prakhar <prakhar@thesys.dev>
Co-authored-by: Subham <subham@thesys.dev>")

 |  |
| 

[.github](/thesysdev/openui/tree/main/.github ".github")

 | 

[.github](/thesysdev/openui/tree/main/.github ".github")

 | 

[Add React-Email + OpenUI Renderer chat (](/thesysdev/openui/commit/999d3a7b00796560ee37920ec51a845319dc9312 "Add React-Email + OpenUI Renderer chat (#371)
* Implement React Email Chat example with OpenAI integration
- Introduced a new example project, `react-email-chat`, showcasing an AI-powered email generator using OpenUI and React Email.
- Added essential configuration files including package.json, ESLint, PostCSS, and TypeScript settings.
- Implemented core components for email generation, including a responsive layout and theme management.
- Established API routes for chat interactions with OpenAI, including a system prompt for generating email content.
- Created a README with setup instructions, features, and component descriptions to facilitate onboarding for developers.
- Included global CSS for consistent styling using Tailwind CSS.
This commit sets the foundation for further development and enhancements in the react-email-chat example.
* Enhance React Email Chat example with new components and functionality
- Introduced `ComposePage` and `ChatPage` components to manage email composition and chat interactions.
- Implemented session management for saving and loading messages and view state using sessionStorage.
- Updated global CSS to style placeholder text for input fields in both light and dark themes.
- Refactored the main `Page` component to integrate new components and improve layout.
- Added utility functions for content parsing and HTML formatting to enhance email rendering capabilities.
- Included loading indicators and conversation starters to improve user experience.
This commit significantly enhances the functionality and user interface of the React Email Chat example.
* Remove React Email Chat example and related configurations
- Deleted the `react-email-chat` example project, including all associated files such as configuration, components, and styles.
- Updated `pnpm-lock.yaml` to reflect the removal of dependencies related to the deleted example.
- Modified `pnpm-workspace.yaml` to exclude the `react-email-chat` package from the workspace.
- Cleaned up environment and configuration files, ensuring no remnants of the removed example remain.
This commit streamlines the project by removing an unused example, improving overall maintainability.
* Refactor and remove React Email Chat package
- Deleted the `react-email-chat` package and its associated files, including configuration and lock files.
- Updated `pnpm-workspace.yaml` to exclude the removed package from the workspace.
- Refactored dependencies in `package.json` to use workspace links for related packages.
- Cleaned up imports in the `react-email-genui` components to streamline code and improve maintainability.
This commit simplifies the project structure by removing the unused `react-email-chat` package and optimizing related configurations.
* Enhance responsiveness in ChatPage and ComposePage components
- Introduced a custom hook, `useIsMobile`, to manage mobile responsiveness based on window width.
- Updated layout and styling in `ChatPage` to include a mobile toggle for HTML and preview views, ensuring a better user experience on smaller screens.
- Adjusted padding, font sizes, and button dimensions in `ComposePage` for improved usability on mobile devices.
- Enhanced grid layout for conversation starters in `ComposePage` to adapt to mobile view, optimizing space and accessibility.
These changes significantly improve the mobile experience for users interacting with the email chat application.
* Enhance ChatPage component for improved mobile responsiveness
- Updated loading indicators to include a spinning animation for mobile devices, enhancing visual feedback during email generation.
- Adjusted button styles and dimensions based on screen size, ensuring a consistent user experience across devices.
- Refined layout properties such as padding and gap to better accommodate mobile users, improving overall usability.
These changes significantly enhance the mobile experience in the ChatPage component, making it more user-friendly and visually appealing.
* Add React Email Chat package with initial setup and components
- Introduced the `react-email-chat` package, including essential configuration files such as `package.json`, `.gitignore`, and `.npmrc`.
- Implemented core components like `ComposePage` and `ChatPage` for managing email interactions.
- Added a new `generate-prompt.ts` script for dynamic prompt generation.
- Updated ESLint configuration to accommodate new rules for specific files.
- Enhanced `next.config.ts` to support turbopack with the correct root directory.
- Created a new `pnpm-lock.yaml` to manage dependencies effectively.
These changes lay the groundwork for further development of the React Email Chat application, enhancing its functionality and maintainability.
* Implement React Email Chat example with comprehensive features
- Added the `react-email-chat` example project, showcasing an AI-powered email generator using OpenUI and React Email.
- Included essential configuration files such as `package.json`, ESLint, PostCSS, and TypeScript settings.
- Developed core components including `ComposePage`, `ChatPage`, and utility functions for content parsing and HTML formatting.
- Established API routes for chat interactions with OpenAI, integrating a system prompt for generating email content.
- Created a README with setup instructions, features, and component descriptions to facilitate onboarding for developers.
- Enhanced global CSS for consistent styling using Tailwind CSS.
These changes lay a solid foundation for further development and enhancements in the React Email Chat example.
* Add TypeScript definitions and update prompt generation in React Email Chat example
- Created a new TypeScript definition file `next-env.d.ts` for the `react-email-chat` example to enhance type safety and integration with Next.js.
- Updated the `generate:prompt` script in `package.json` to reference the new `chat-library.tsx` file, improving prompt generation functionality.
- Removed the obsolete `.gitkeep` file from the `src/generated` directory and added a new `system-prompt.txt` file containing the AI assistant's response guidelines.
These changes improve the structure and functionality of the React Email Chat example, ensuring better type support and prompt management.
* Refactor React Email Chat example by removing unused components and updating dependencies
- Removed the `@openuidev/react-ui` dependency from the `react-email-chat` example, streamlining the project.
- Updated the `generate:prompt` script to reference the new `library.ts` file, enhancing prompt generation functionality.
- Refactored the `ChatPage` and `ComposePage` components to improve structure and maintainability.
- Replaced the obsolete `chat-library.tsx` with a new `library.ts` that consolidates email-related components and utilities.
- Enhanced the `pnpm-lock.yaml` to reflect updated dependencies and ensure consistency across the project.
These changes improve the overall organization and functionality of the React Email Chat example, ensuring better integration and performance.
* Refactor EmailApp component in React Email Chat example for improved session management
- Removed the `ready` state and adjusted the session restoration logic to occur synchronously on the first render, enhancing performance and reducing complexity.
- Updated the `restoredRef` to use a nullable boolean type for better clarity in state management.
- Deleted the unused `library.ts` file, streamlining the project by removing unnecessary code.
These changes enhance the overall efficiency and maintainability of the EmailApp component in the React Email Chat example.
* Refactor imports in library.ts for improved organization
- Rearranged and updated component imports in `library.ts` to enhance clarity and maintainability.
- Moved `EmailCard` import above `FollowUpItem` and adjusted the order of form component imports for better structure.
These changes streamline the import section of the file, making it easier to navigate and manage component dependencies.
* Update dependencies and clean up React Email Chat example
- Removed the `lucide-react` dependency from both `package.json` files in the `react-email` and `react-email-chat` examples, streamlining the project.
- Updated the `generate:prompt` script in the `react-email-chat` example to provide a static message instead of generating a prompt dynamically.
- Refactored the `render-email.tsx` file by removing unused components, enhancing code clarity and maintainability.
- Updated the `pnpm-lock.yaml` to reflect the changes in dependencies and ensure consistency across the project.
These changes improve the overall organization and functionality of the React Email Chat example, ensuring better integration and performance.
* Refactor React Email Chat components and update dependencies
- Removed the `@react-email/render` dependency from `package.json` and updated the `pnpm-lock.yaml` to reflect this change, streamlining the project.
- Refactored the `ChatPage` component to use the new `emailChatLibrary` instead of the deprecated `emailLibrary`, enhancing code clarity.
- Updated the `system-prompt.txt` to reflect changes in the email generation process, including the new root component definition.
- Introduced new components such as `EmailCard`, `FollowUpBlock`, and `TextContent` to improve the structure and functionality of the chat interface.
These changes enhance the overall organization and performance of the React Email Chat example, ensuring better integration and user experience.
* Enhance React Email Chat functionality and update components
- Updated the `generate:prompt` script in `package.json` to generate the system prompt dynamically, improving the email generation process.
- Changed the model used in the chat API from "gpt-4o" to "gpt-5.4" for enhanced performance.
- Implemented user scroll tracking in the `ChatPage` component to improve user experience during email generation.
- Expanded the `STARTERS` array with new email templates, including a launch announcement and an abandoned cart reminder, to provide users with more options.
- Updated the `system-prompt.txt` to reflect changes in the email generation capabilities, ensuring accurate guidance for the AI.
These changes enhance the overall functionality and user experience of the React Email Chat example, making it more robust and user-friendly.
* Refactor React Email Chat to utilize new email library and clean up code
- Updated the `generate:prompt` script in `package.json` to use the new `emailLibrary` from `@openuidev/react-email`, enhancing prompt generation.
- Replaced instances of `emailChatLibrary` with `emailLibrary` in the `ChatPage` component for consistency and improved functionality.
- Removed the deprecated `chat-library.tsx` file, streamlining the project structure and reducing complexity.
- Cleaned up imports in `index.ts` to improve organization and maintainability.
These changes enhance the overall functionality and clarity of the React Email Chat example, ensuring better integration with the updated email library.
* Add React Email example with new components and features
- Introduced the `react-email` example, showcasing an AI-powered email generator using OpenUI and React Email.
- Added a new `react-email` component library with 44 email components for dynamic email generation.
- Implemented a live preview feature that allows users to see email designs in real-time as they describe them.
- Created a README with setup instructions, features, and project structure to assist developers.
- Included necessary configuration files such as `package.json`, ESLint, PostCSS, and TypeScript settings.
These changes enhance the functionality and usability of the React Email example, providing a robust foundation for future enhancements.
* Update pnpm-lock.yaml to reflect dependency changes and version updates
- Updated `eslint` from version 10.0.2 to 9.29.0 in multiple dependencies to ensure compatibility and stability.
- Changed the `resolve` package version from 1.22.10 to 1.22.11 for minor improvements.
- Removed the `zod` dependency from the project, streamlining the dependency list.
- Renamed the `examples/react-email-chat` directory to `examples/react-email` for clarity and consistency.
These changes enhance the overall dependency management and organization of the project.
* Add lucide-react dependency and refactor email components
- Introduced `lucide-react` as a dependency in `package.json` for improved icon usage.
- Replaced the `ChatPage` component with a new `EmailEditor` component to enhance email composition functionality.
- Updated the `compose-page.tsx` to utilize the new `Send` icon from `lucide-react`.
- Removed unused components such as `content-parser.ts`, `format-html.ts`, and `icons.tsx` to streamline the project structure.
These changes improve the overall functionality and organization of the React Email example, providing a more robust email editing experience.
* Remove deprecated render-email.tsx file and update EmailEditor to use new rendering method
- Deleted the `render-email.tsx` file to eliminate unused code and streamline the project.
- Updated the `EmailEditor` component to utilize the new rendering method from `@react-email/render`, enhancing the email generation process.
- Adjusted the onStreamingEnd callback to reflect the new rendering logic, improving overall functionality.
These changes enhance the clarity and performance of the React Email example, ensuring better integration with the updated rendering approach.
* Refactor email components and update imports for consistency
- Updated import paths in `layout.tsx` and `page.tsx` to use camelCase for `useSystemTheme`, `composePage`, and `emailEditor`.
- Removed the deprecated `email-editor.tsx` file to streamline the project structure.
- Introduced new components: `LoadingDots`, `ComposePage`, and various email editor components to enhance functionality and user experience.
These changes improve code consistency and organization, providing a more robust email editing experience.
* Update React Email example documentation and structure
- Clarified the usage of the `useEmailRendering` hook in the `react-email.mdx` file to specify client-side rendering.
- Improved the README with prerequisites, setup instructions, and key dependencies for better onboarding.
- Enhanced project structure by organizing components into dedicated directories for better maintainability.
- Updated commands for starting the development server to reflect the new directory structure.
These changes improve clarity and usability for developers working with the React Email example.
* Add tsx dependency to React Email example
- Updated `pnpm-lock.yaml` to include `tsx` version 4.20.3 for improved TypeScript support.
- Added `tsx` as a dependency in `examples/react-email/package.json` to ensure compatibility with the latest features.
These changes enhance the development experience by integrating the latest TypeScript tooling.
* Refactor theme handling and streamline email components
- Removed the `useSystemTheme` hook and its associated `ThemeProvider` to simplify theme management in the application.
- Updated `ComposePage` and `EmailEditor` components to use a hardcoded dark mode instead of dynamic theme detection.
- Adjusted the `useEmailRendering` hook to remove unnecessary checks related to the `openuiCode` variable.
- Enhanced the `CodeBlock` component to ensure default language handling is more robust.
These changes improve the overall code clarity and reduce complexity in theme management across the React Email example.
* Refactor email component organization and structure
- Moved email components and their associated groups from `index.ts` to a new `library.ts` file for better modularity and maintainability.
- This restructuring enhances the clarity of the email component library, making it easier to manage and extend in the future.
These changes improve the overall organization of the React Email example, facilitating easier access to components and their documentation.
* Enhance React Email package and workflow configuration
- Updated the GitHub Actions workflow to include 'react-email' as a publishable package option.
- Added new linting and formatting scripts to the `react-email` package for improved code quality checks.
- Refactored the `CustomerReview` component for better readability by adjusting code formatting.
These changes improve the development workflow and maintainability of the React Email package.")[#371](https://github.com/thesysdev/openui/pull/371)[)](/thesysdev/openui/commit/999d3a7b00796560ee37920ec51a845319dc9312 "Add React-Email + OpenUI Renderer chat (#371)
* Implement React Email Chat example with OpenAI integration
- Introduced a new example project, `react-email-chat`, showcasing an AI-powered email generator using OpenUI and React Email.
- Added essential configuration files including package.json, ESLint, PostCSS, and TypeScript settings.
- Implemented core components for email generation, including a responsive layout and theme management.
- Established API routes for chat interactions with OpenAI, including a system prompt for generating email content.
- Created a README with setup instructions, features, and component descriptions to facilitate onboarding for developers.
- Included global CSS for consistent styling using Tailwind CSS.
This commit sets the foundation for further development and enhancements in the react-email-chat example.
* Enhance React Email Chat example with new components and functionality
- Introduced `ComposePage` and `ChatPage` components to manage email composition and chat interactions.
- Implemented session management for saving and loading messages and view state using sessionStorage.
- Updated global CSS to style placeholder text for input fields in both light and dark themes.
- Refactored the main `Page` component to integrate new components and improve layout.
- Added utility functions for content parsing and HTML formatting to enhance email rendering capabilities.
- Included loading indicators and conversation starters to improve user experience.
This commit significantly enhances the functionality and user interface of the React Email Chat example.
* Remove React Email Chat example and related configurations
- Deleted the `react-email-chat` example project, including all associated files such as configuration, components, and styles.
- Updated `pnpm-lock.yaml` to reflect the removal of dependencies related to the deleted example.
- Modified `pnpm-workspace.yaml` to exclude the `react-email-chat` package from the workspace.
- Cleaned up environment and configuration files, ensuring no remnants of the removed example remain.
This commit streamlines the project by removing an unused example, improving overall maintainability.
* Refactor and remove React Email Chat package
- Deleted the `react-email-chat` package and its associated files, including configuration and lock files.
- Updated `pnpm-workspace.yaml` to exclude the removed package from the workspace.
- Refactored dependencies in `package.json` to use workspace links for related packages.
- Cleaned up imports in the `react-email-genui` components to streamline code and improve maintainability.
This commit simplifies the project structure by removing the unused `react-email-chat` package and optimizing related configurations.
* Enhance responsiveness in ChatPage and ComposePage components
- Introduced a custom hook, `useIsMobile`, to manage mobile responsiveness based on window width.
- Updated layout and styling in `ChatPage` to include a mobile toggle for HTML and preview views, ensuring a better user experience on smaller screens.
- Adjusted padding, font sizes, and button dimensions in `ComposePage` for improved usability on mobile devices.
- Enhanced grid layout for conversation starters in `ComposePage` to adapt to mobile view, optimizing space and accessibility.
These changes significantly improve the mobile experience for users interacting with the email chat application.
* Enhance ChatPage component for improved mobile responsiveness
- Updated loading indicators to include a spinning animation for mobile devices, enhancing visual feedback during email generation.
- Adjusted button styles and dimensions based on screen size, ensuring a consistent user experience across devices.
- Refined layout properties such as padding and gap to better accommodate mobile users, improving overall usability.
These changes significantly enhance the mobile experience in the ChatPage component, making it more user-friendly and visually appealing.
* Add React Email Chat package with initial setup and components
- Introduced the `react-email-chat` package, including essential configuration files such as `package.json`, `.gitignore`, and `.npmrc`.
- Implemented core components like `ComposePage` and `ChatPage` for managing email interactions.
- Added a new `generate-prompt.ts` script for dynamic prompt generation.
- Updated ESLint configuration to accommodate new rules for specific files.
- Enhanced `next.config.ts` to support turbopack with the correct root directory.
- Created a new `pnpm-lock.yaml` to manage dependencies effectively.
These changes lay the groundwork for further development of the React Email Chat application, enhancing its functionality and maintainability.
* Implement React Email Chat example with comprehensive features
- Added the `react-email-chat` example project, showcasing an AI-powered email generator using OpenUI and React Email.
- Included essential configuration files such as `package.json`, ESLint, PostCSS, and TypeScript settings.
- Developed core components including `ComposePage`, `ChatPage`, and utility functions for content parsing and HTML formatting.
- Established API routes for chat interactions with OpenAI, integrating a system prompt for generating email content.
- Created a README with setup instructions, features, and component descriptions to facilitate onboarding for developers.
- Enhanced global CSS for consistent styling using Tailwind CSS.
These changes lay a solid foundation for further development and enhancements in the React Email Chat example.
* Add TypeScript definitions and update prompt generation in React Email Chat example
- Created a new TypeScript definition file `next-env.d.ts` for the `react-email-chat` example to enhance type safety and integration with Next.js.
- Updated the `generate:prompt` script in `package.json` to reference the new `chat-library.tsx` file, improving prompt generation functionality.
- Removed the obsolete `.gitkeep` file from the `src/generated` directory and added a new `system-prompt.txt` file containing the AI assistant's response guidelines.
These changes improve the structure and functionality of the React Email Chat example, ensuring better type support and prompt management.
* Refactor React Email Chat example by removing unused components and updating dependencies
- Removed the `@openuidev/react-ui` dependency from the `react-email-chat` example, streamlining the project.
- Updated the `generate:prompt` script to reference the new `library.ts` file, enhancing prompt generation functionality.
- Refactored the `ChatPage` and `ComposePage` components to improve structure and maintainability.
- Replaced the obsolete `chat-library.tsx` with a new `library.ts` that consolidates email-related components and utilities.
- Enhanced the `pnpm-lock.yaml` to reflect updated dependencies and ensure consistency across the project.
These changes improve the overall organization and functionality of the React Email Chat example, ensuring better integration and performance.
* Refactor EmailApp component in React Email Chat example for improved session management
- Removed the `ready` state and adjusted the session restoration logic to occur synchronously on the first render, enhancing performance and reducing complexity.
- Updated the `restoredRef` to use a nullable boolean type for better clarity in state management.
- Deleted the unused `library.ts` file, streamlining the project by removing unnecessary code.
These changes enhance the overall efficiency and maintainability of the EmailApp component in the React Email Chat example.
* Refactor imports in library.ts for improved organization
- Rearranged and updated component imports in `library.ts` to enhance clarity and maintainability.
- Moved `EmailCard` import above `FollowUpItem` and adjusted the order of form component imports for better structure.
These changes streamline the import section of the file, making it easier to navigate and manage component dependencies.
* Update dependencies and clean up React Email Chat example
- Removed the `lucide-react` dependency from both `package.json` files in the `react-email` and `react-email-chat` examples, streamlining the project.
- Updated the `generate:prompt` script in the `react-email-chat` example to provide a static message instead of generating a prompt dynamically.
- Refactored the `render-email.tsx` file by removing unused components, enhancing code clarity and maintainability.
- Updated the `pnpm-lock.yaml` to reflect the changes in dependencies and ensure consistency across the project.
These changes improve the overall organization and functionality of the React Email Chat example, ensuring better integration and performance.
* Refactor React Email Chat components and update dependencies
- Removed the `@react-email/render` dependency from `package.json` and updated the `pnpm-lock.yaml` to reflect this change, streamlining the project.
- Refactored the `ChatPage` component to use the new `emailChatLibrary` instead of the deprecated `emailLibrary`, enhancing code clarity.
- Updated the `system-prompt.txt` to reflect changes in the email generation process, including the new root component definition.
- Introduced new components such as `EmailCard`, `FollowUpBlock`, and `TextContent` to improve the structure and functionality of the chat interface.
These changes enhance the overall organization and performance of the React Email Chat example, ensuring better integration and user experience.
* Enhance React Email Chat functionality and update components
- Updated the `generate:prompt` script in `package.json` to generate the system prompt dynamically, improving the email generation process.
- Changed the model used in the chat API from "gpt-4o" to "gpt-5.4" for enhanced performance.
- Implemented user scroll tracking in the `ChatPage` component to improve user experience during email generation.
- Expanded the `STARTERS` array with new email templates, including a launch announcement and an abandoned cart reminder, to provide users with more options.
- Updated the `system-prompt.txt` to reflect changes in the email generation capabilities, ensuring accurate guidance for the AI.
These changes enhance the overall functionality and user experience of the React Email Chat example, making it more robust and user-friendly.
* Refactor React Email Chat to utilize new email library and clean up code
- Updated the `generate:prompt` script in `package.json` to use the new `emailLibrary` from `@openuidev/react-email`, enhancing prompt generation.
- Replaced instances of `emailChatLibrary` with `emailLibrary` in the `ChatPage` component for consistency and improved functionality.
- Removed the deprecated `chat-library.tsx` file, streamlining the project structure and reducing complexity.
- Cleaned up imports in `index.ts` to improve organization and maintainability.
These changes enhance the overall functionality and clarity of the React Email Chat example, ensuring better integration with the updated email library.
* Add React Email example with new components and features
- Introduced the `react-email` example, showcasing an AI-powered email generator using OpenUI and React Email.
- Added a new `react-email` component library with 44 email components for dynamic email generation.
- Implemented a live preview feature that allows users to see email designs in real-time as they describe them.
- Created a README with setup instructions, features, and project structure to assist developers.
- Included necessary configuration files such as `package.json`, ESLint, PostCSS, and TypeScript settings.
These changes enhance the functionality and usability of the React Email example, providing a robust foundation for future enhancements.
* Update pnpm-lock.yaml to reflect dependency changes and version updates
- Updated `eslint` from version 10.0.2 to 9.29.0 in multiple dependencies to ensure compatibility and stability.
- Changed the `resolve` package version from 1.22.10 to 1.22.11 for minor improvements.
- Removed the `zod` dependency from the project, streamlining the dependency list.
- Renamed the `examples/react-email-chat` directory to `examples/react-email` for clarity and consistency.
These changes enhance the overall dependency management and organization of the project.
* Add lucide-react dependency and refactor email components
- Introduced `lucide-react` as a dependency in `package.json` for improved icon usage.
- Replaced the `ChatPage` component with a new `EmailEditor` component to enhance email composition functionality.
- Updated the `compose-page.tsx` to utilize the new `Send` icon from `lucide-react`.
- Removed unused components such as `content-parser.ts`, `format-html.ts`, and `icons.tsx` to streamline the project structure.
These changes improve the overall functionality and organization of the React Email example, providing a more robust email editing experience.
* Remove deprecated render-email.tsx file and update EmailEditor to use new rendering method
- Deleted the `render-email.tsx` file to eliminate unused code and streamline the project.
- Updated the `EmailEditor` component to utilize the new rendering method from `@react-email/render`, enhancing the email generation process.
- Adjusted the onStreamingEnd callback to reflect the new rendering logic, improving overall functionality.
These changes enhance the clarity and performance of the React Email example, ensuring better integration with the updated rendering approach.
* Refactor email components and update imports for consistency
- Updated import paths in `layout.tsx` and `page.tsx` to use camelCase for `useSystemTheme`, `composePage`, and `emailEditor`.
- Removed the deprecated `email-editor.tsx` file to streamline the project structure.
- Introduced new components: `LoadingDots`, `ComposePage`, and various email editor components to enhance functionality and user experience.
These changes improve code consistency and organization, providing a more robust email editing experience.
* Update React Email example documentation and structure
- Clarified the usage of the `useEmailRendering` hook in the `react-email.mdx` file to specify client-side rendering.
- Improved the README with prerequisites, setup instructions, and key dependencies for better onboarding.
- Enhanced project structure by organizing components into dedicated directories for better maintainability.
- Updated commands for starting the development server to reflect the new directory structure.
These changes improve clarity and usability for developers working with the React Email example.
* Add tsx dependency to React Email example
- Updated `pnpm-lock.yaml` to include `tsx` version 4.20.3 for improved TypeScript support.
- Added `tsx` as a dependency in `examples/react-email/package.json` to ensure compatibility with the latest features.
These changes enhance the development experience by integrating the latest TypeScript tooling.
* Refactor theme handling and streamline email components
- Removed the `useSystemTheme` hook and its associated `ThemeProvider` to simplify theme management in the application.
- Updated `ComposePage` and `EmailEditor` components to use a hardcoded dark mode instead of dynamic theme detection.
- Adjusted the `useEmailRendering` hook to remove unnecessary checks related to the `openuiCode` variable.
- Enhanced the `CodeBlock` component to ensure default language handling is more robust.
These changes improve the overall code clarity and reduce complexity in theme management across the React Email example.
* Refactor email component organization and structure
- Moved email components and their associated groups from `index.ts` to a new `library.ts` file for better modularity and maintainability.
- This restructuring enhances the clarity of the email component library, making it easier to manage and extend in the future.
These changes improve the overall organization of the React Email example, facilitating easier access to components and their documentation.
* Enhance React Email package and workflow configuration
- Updated the GitHub Actions workflow to include 'react-email' as a publishable package option.
- Added new linting and formatting scripts to the `react-email` package for improved code quality checks.
- Refactored the `CustomerReview` component for better readability by adjusting code formatting.
These changes improve the development workflow and maintainability of the React Email package.")

 |  |
| 

[assets](/thesysdev/openui/tree/main/assets "assets")

 | 

[assets](/thesysdev/openui/tree/main/assets "assets")

 |  |  |
| 

[benchmarks](/thesysdev/openui/tree/main/benchmarks "benchmarks")

 | 

[benchmarks](/thesysdev/openui/tree/main/benchmarks "benchmarks")

 | 

[Include YAML in the benchmark (](/thesysdev/openui/commit/47c86e023451cd2017e96dba55f3e5756eb342bf "Include YAML in the benchmark (#337)")[#337](https://github.com/thesysdev/openui/pull/337)[)](/thesysdev/openui/commit/47c86e023451cd2017e96dba55f3e5756eb342bf "Include YAML in the benchmark (#337)")

 |  |
| 

[docs](/thesysdev/openui/tree/main/docs "docs")

 | 

[docs](/thesysdev/openui/tree/main/docs "docs")

 | 

[Enhance API reference for React Email package (](/thesysdev/openui/commit/2c8e91b58f42837f367799ec32ebac7050a30ebc "Enhance API reference for React Email package (#387)
* Enhance API reference for React Email package
- Updated the main API reference to include @openuidev/react-email, detailing its components and usage.
- Added a new documentation file for the @openuidev/react-email package, outlining its features, components, and examples for LLM-driven email generation.
- Modified meta.json files to include the new package in the documentation structure.
- Updated package.json for @openuidev/react-email to reflect version changes and include necessary files for distribution.
* Update API reference for @openuidev/react-email package
- Revised descriptions in the API reference to clarify the purpose of the package and its components.
- Changed the installation instructions to reflect the correct package usage.
- Streamlined the documentation for email generation features, emphasizing the pre-built templates and prompt options.
- Enhanced the README to provide a clearer overview of the package's capabilities and installation steps.")[#387](https://github.com/thesysdev/openui/pull/387)[)](/thesysdev/openui/commit/2c8e91b58f42837f367799ec32ebac7050a30ebc "Enhance API reference for React Email package (#387)
* Enhance API reference for React Email package
- Updated the main API reference to include @openuidev/react-email, detailing its components and usage.
- Added a new documentation file for the @openuidev/react-email package, outlining its features, components, and examples for LLM-driven email generation.
- Modified meta.json files to include the new package in the documentation structure.
- Updated package.json for @openuidev/react-email to reflect version changes and include necessary files for distribution.
* Update API reference for @openuidev/react-email package
- Revised descriptions in the API reference to clarify the purpose of the package and its components.
- Changed the installation instructions to reflect the correct package usage.
- Streamlined the documentation for email generation features, emphasizing the pre-built templates and prompt options.
- Enhanced the README to provide a clearer overview of the package's capabilities and installation steps.")

 |  |
| 

[examples](/thesysdev/openui/tree/main/examples "examples")

 | 

[examples](/thesysdev/openui/tree/main/examples "examples")

 | 

[Add @openuidev/svelte-lang and extract @openuidev/lang-core (](/thesysdev/openui/commit/46345076b16a824b0992b210733ba957a1175549 "Add @openuidev/svelte-lang and extract @openuidev/lang-core (#347)
* Extract framework-agnostic core into lang-core package
Move parser, prompt generation, validation, and generic library
types out of react-lang into a new @openuidev/lang-core package.
The generic DefinedComponent<T, C = unknown> and Library<C> allow
each framework adapter (React, Svelte, etc.) to narrow the component
type parameter independently.
* Update react-lang to use lang-core
Replace local parser, prompt, and validation code with imports from
@openuidev/lang-core. The library.ts becomes a thin wrapper that
narrows the generic C parameter to React.FC<ComponentRenderProps>.
Public API is unchanged — all existing examples build without
modification.
* Add Svelte 5 renderer (svelte-lang)
Introduce @openuidev/svelte-lang — a Svelte 5 port of react-lang
built on top of @openuidev/lang-core. Uses runes ($state, $derived,
$effect, $props), snippets for renderNode, getContext/setContext for
the OpenUI context, and <svelte:boundary> for error handling.
Includes 30 passing tests.
* Add svelte-chat example
A SvelteKit demo app showing @openuidev/svelte-lang in action with
mock streaming, four components (Stack, Card, TextContent, Button),
and action event handling. No API key required. Also add .svelte-kit
to .gitignore.
* Add eslint/tsconfig.test setup and move parser tests to lang-core
This covers:
- New eslint.config.cjs and tsconfig.test.json for lang-core (matching react-lang pattern)
- Parser test file moved from react-lang to lang-core
- package.json updated with vitest dev dependency and formatting
- src/index.ts export updated (ValidationError → ValidationErrorCode)")[#347](https://github.com/thesysdev/openui/pull/347)[)](/thesysdev/openui/commit/46345076b16a824b0992b210733ba957a1175549 "Add @openuidev/svelte-lang and extract @openuidev/lang-core (#347)
* Extract framework-agnostic core into lang-core package
Move parser, prompt generation, validation, and generic library
types out of react-lang into a new @openuidev/lang-core package.
The generic DefinedComponent<T, C = unknown> and Library<C> allow
each framework adapter (React, Svelte, etc.) to narrow the component
type parameter independently.
* Update react-lang to use lang-core
Replace local parser, prompt, and validation code with imports from
@openuidev/lang-core. The library.ts becomes a thin wrapper that
narrows the generic C parameter to React.FC<ComponentRenderProps>.
Public API is unchanged — all existing examples build without
modification.
* Add Svelte 5 renderer (svelte-lang)
Introduce @openuidev/svelte-lang — a Svelte 5 port of react-lang
built on top of @openuidev/lang-core. Uses runes ($state, $derived,
$effect, $props), snippets for renderNode, getContext/setContext for
the OpenUI context, and <svelte:boundary> for error handling.
Includes 30 passing tests.
* Add svelte-chat example
A SvelteKit demo app showing @openuidev/svelte-lang in action with
mock streaming, four components (Stack, Card, TextContent, Button),
and action event handling. No API key required. Also add .svelte-kit
to .gitignore.
* Add eslint/tsconfig.test setup and move parser tests to lang-core
This covers:
- New eslint.config.cjs and tsconfig.test.json for lang-core (matching react-lang pattern)
- Parser test file moved from react-lang to lang-core
- package.json updated with vitest dev dependency and formatting
- src/index.ts export updated (ValidationError → ValidationErrorCode)")

 |  |
| 

[packages](/thesysdev/openui/tree/main/packages "packages")

 | 

[packages](/thesysdev/openui/tree/main/packages "packages")

 | 

[Bump versions: react-headless, react-lang, react-ui, openui-cli (](/thesysdev/openui/commit/bca62da322f2abffbaf86431af35c1a464c1d01e "Bump versions: react-headless, react-lang, react-ui, openui-cli (#397)")[#397](https://github.com/thesysdev/openui/pull/397)[)](/thesysdev/openui/commit/bca62da322f2abffbaf86431af35c1a464c1d01e "Bump versions: react-headless, react-lang, react-ui, openui-cli (#397)")

 |  |
| 

[skills/ openui](/thesysdev/openui/tree/main/skills/openui "This path skips through empty directories")

 | 

[skills/ openui](/thesysdev/openui/tree/main/skills/openui "This path skips through empty directories")

 | 

[Add Agent Skill for OpenUI (](/thesysdev/openui/commit/d982a4154451463de523f056812d423d7b65ad55 "Add Agent Skill for OpenUI (#343)
Improve documentation and add a skill for OpenUI
Co-authored-by: Claude Sonnet 4.6 <noreply@anthropic.com>")[#343](https://github.com/thesysdev/openui/pull/343)[)](/thesysdev/openui/commit/d982a4154451463de523f056812d423d7b65ad55 "Add Agent Skill for OpenUI (#343)
Improve documentation and add a skill for OpenUI
Co-authored-by: Claude Sonnet 4.6 <noreply@anthropic.com>")

 |  |
| 

[.cursorignore](/thesysdev/openui/blob/main/.cursorignore ".cursorignore")

 | 

[.cursorignore](/thesysdev/openui/blob/main/.cursorignore ".cursorignore")

 |  |  |
| 

[.dockerignore](/thesysdev/openui/blob/main/.dockerignore ".dockerignore")

 | 

[.dockerignore](/thesysdev/openui/blob/main/.dockerignore ".dockerignore")

 | 

[fix: Dockerfile for openui-chat with pnpm workspace support (](/thesysdev/openui/commit/bf933112d09d581c0108f03f0ec9f2bc7ddd996b "fix: Dockerfile for openui-chat with pnpm workspace support (#370)
* fix(openui-chat): monorepo-safe Docker build and standalone runtime paths
* docs: add Docker usage for openui-chat
* fix: correct Alpine user creation for runtime
* fix: update Docker usage to support example directory")[#370](https://github.com/thesysdev/openui/pull/370)[)](/thesysdev/openui/commit/bf933112d09d581c0108f03f0ec9f2bc7ddd996b "fix: Dockerfile for openui-chat with pnpm workspace support (#370)
* fix(openui-chat): monorepo-safe Docker build and standalone runtime paths
* docs: add Docker usage for openui-chat
* fix: correct Alpine user creation for runtime
* fix: update Docker usage to support example directory")

 |  |
|  |

OpenUI is a full-stack Generative UI framework — a compact streaming-first language, a React runtime with built-in component libraries, and ready-to-use chat interfaces — that is up to 67% more token-efficient than JSON.

* * *

[Docs](https://openui.com) · [Playground](https://www.openui.com/playground) · [Sample Chat App](/thesysdev/openui/blob/main/examples/openui-chat) · [Discord](https://discord.com/invite/Pbv5PsqUSv) · [Contributing](/thesysdev/openui/blob/main/CONTRIBUTING.md) · [Code of Conduct](/thesysdev/openui/blob/main/CODE_OF_CONDUCT.md) · [Security](/thesysdev/openui/blob/main/SECURITY.md) · [License](/thesysdev/openui/blob/main/LICENSE)

* * *

[![OpenUI Demo](/thesysdev/openui/raw/main/assets/demo.gif)](/thesysdev/openui/blob/main/assets/demo.gif)

At the center of OpenUI is **OpenUI Lang**: a compact, streaming-first language for model-generated UI. Instead of treating model output as only text, OpenUI lets you define components, generate prompt instructions from that component library, and render structured UI as the model streams.

**Core capabilities:**

- **OpenUI Lang** — A compact language for structured UI generation designed for streaming output.
- **Built-in component libraries** — Charts, forms, tables, layouts, and more — ready to use or extend.
- **Prompt generation from your component library** — Generate model instructions directly from the components you allow.
- **Streaming renderer** — Parse and render model output progressively in React as tokens arrive.
- **Chat and app surfaces** - Use the same foundation for assistants, copilots, and broader interactive product flows.

## Quick Start

```
npx @openuidev/cli@latest create --name genui-chat-app
cd genui-chat-app
echo "OPENAI_API_KEY=sk-your-key-here" > .env
npm run dev
```

This is the fastest way to start with OpenUI. The scaffolded app gives you an end-to-end starting point with streaming, built-in UI, and OpenUI Lang support.

What this gives you:

- **OpenUI Lang support** - Start with structured UI generation built into the app flow.
- **Library-driven prompts** - Generate instructions from your allowed component set.
- **Streaming support** - Update the UI progressively as output arrives.
- **Working app foundation** - Start from a ready-to-run example instead of wiring everything manually.

Your components define what the model can generate.

```
flowchart LR
 A["Component Library"] --> B["System Prompt"]
 B --> C["LLM"]
 C --> D["OpenUI Lang Stream"]
 D --> E["Renderer"]
 E --> F["Live UI"]
```

1.  Define or reuse a component library.
2.  Generate a system prompt from that library.
3.  Send that prompt to your model.
4.  Stream OpenUI Lang output back to the client.
5.  Render the output progressively with Renderer.

Try it yourself in the [Playground](https://www.openui.com/playground) — generate UI live with the default component library.

## Packages

| Package | Description |
| :-- | :-- |
| [`@openuidev/react-lang`](/thesysdev/openui/blob/main/packages/react-lang) | Core runtime — component definitions, parser, renderer, prompt generation |
| [`@openuidev/react-headless`](/thesysdev/openui/blob/main/packages/react-headless) | Headless chat state, streaming adapters, message format converters |
| [`@openuidev/react-ui`](/thesysdev/openui/blob/main/packages/react-ui) | Prebuilt chat layouts and two built-in component libraries |
| [`@openuidev/cli`](/thesysdev/openui/blob/main/packages/openui-cli) | CLI for scaffolding apps and generating system prompts |

```
npm install @openuidev/react-lang @openuidev/react-ui
```

OpenUI Lang is designed for model-generated UI that needs to be both structured and streamable.

- **Streaming output** — Emit UI incrementally as tokens arrive.
- **Token efficiency** — Up to 67% fewer tokens than equivalent JSON (see [benchmarks](/thesysdev/openui/blob/main/benchmarks)).
- **Controlled rendering** — Restrict output to the components you define and register.
- **Typed component contracts** — Define component props and structure up front with Zod schemas.

Measured with `tiktoken` (GPT-5 encoder). OpenUI Lang vs two JSON-based streaming formats across seven UI scenarios:

| Scenario | Vercel JSON-Render | Thesys C1 JSON | OpenUI Lang | vs Vercel | vs C1 |
| --- | --: | --: | --: | --: | --: |
| simple-table | 340 | 357 | 148 | \-56.5% | \-58.5% |
| chart-with-data | 520 | 516 | 231 | \-55.6% | \-55.2% |
| contact-form | 893 | 849 | 294 | \-67.1% | \-65.4% |
| dashboard | 2247 | 2261 | 1226 | \-45.4% | \-45.8% |
| pricing-page | 2487 | 2379 | 1195 | \-52.0% | \-49.8% |
| settings-panel | 1244 | 1205 | 540 | \-56.6% | \-55.2% |
| e-commerce-product | 2449 | 2381 | 1166 | \-52.4% | \-51.0% |
| **TOTAL** | **10180** | **9948** | **4800** | **\-52.8%** | **\-51.7%** |

Full methodology and reproduction steps in [`benchmarks/`](/thesysdev/openui/blob/main/benchmarks).

## Documentation

Detailed documentation is available at [openui.com](https://openui.com).

## Repository structure

```
openui/
├── packages/
│ ├── react-lang/ # Core runtime (parser, renderer, prompt generation)
│ ├── react-headless/ # Headless chat state & streaming adapters
│ ├── react-ui/ # Prebuilt chat layouts & component libraries
│ └── openui-cli/ # CLI for scaffolding & prompt generation
├── skills/
│ └── openui/ # Claude Code skill for AI-assisted development
├── examples/
│ └── openui-chat/ # Full working example app (Next.js)
├── docs/ # Documentation site (openui.com)
└── benchmarks/ # Token efficiency benchmarks
```

Good places to start:

- [openui.com](https://openui.com) for the full docs
- [`examples/openui-chat`](/thesysdev/openui/blob/main/examples/openui-chat) for a working app
- [`CONTRIBUTING.md`](/thesysdev/openui/blob/main/CONTRIBUTING.md) if you want to contribute

## Community

- [Discord](https://discord.com/invite/Pbv5PsqUSv) — Ask questions, share what you're building
- [GitHub Issues](https://github.com/thesysdev/openui/issues) — Report bugs or request features

## Contributing

Contributions are welcome. See [`CONTRIBUTING.md`](/thesysdev/openui/blob/main/CONTRIBUTING.md) for contribution guidelines and ways to get involved.

## Agent Skill

OpenUI ships an [Agent Skill](https://agentskills.io) so AI coding assistants (Claude Code, Codex, Cursor, Copilot, etc.) can help you scaffold, build, and debug Generative UI apps using OpenUI Lang.

### Install

```
# With the skills CLI (works across all agents)
npx skills add thesysdev/openui --skill openui
 
# Manual — copy into your project
cp -r skills/openui .claude/skills/openui
```

The skill covers component library design, OpenUI Lang syntax, system prompt generation, the Renderer, SDK packages, and debugging malformed LLM output.

## License

This project is available under the terms described in [`LICENSE`](/thesysdev/openui/blob/main/LICENSE).

## Releases

No releases published

## Languages

- [TypeScript 85.7%](/thesysdev/openui/search?l=typescript)
- [SCSS 10.8%](/thesysdev/openui/search?l=scss)
- [MDX 2.4%](/thesysdev/openui/search?l=mdx)
- Other 1.1%

* * *

# vercel-labs/json-render: The Generative UI framework

https://github.com/vercel-labs/json-render

[Open in github.dev](https://github.dev/) [Open in a new github.dev tab](https://github.dev/) [Open in codespace](/codespaces/new/vercel-labs/json-render?resume=1)

| Name | Name | 
Last commit message

 | 

Last commit date

 |
| --- | --- | --- | --- |
| 

[40892a6](/vercel-labs/json-render/commit/40892a6af0b99d64ebc8415bd72544ef11b964fa) ·

[191 Commits](/vercel-labs/json-render/commits/main/)

 |
| 

[.changeset](/vercel-labs/json-render/tree/main/.changeset ".changeset")

 | 

[.changeset](/vercel-labs/json-render/tree/main/.changeset ".changeset")

 |  |  |
| 

[.cursor](/vercel-labs/json-render/tree/main/.cursor ".cursor")

 | 

[.cursor](/vercel-labs/json-render/tree/main/.cursor ".cursor")

 | 

[mcp (](/vercel-labs/json-render/commit/1cc87310c90d65ff2c93a97b58acd91d231c2e0f "mcp (#184)
* mcp
* fix lint")[#184](https://github.com/vercel-labs/json-render/pull/184)[)](/vercel-labs/json-render/commit/1cc87310c90d65ff2c93a97b58acd91d231c2e0f "mcp (#184)
* mcp
* fix lint")

 |  |
| 

[.github/ workflows](/vercel-labs/json-render/tree/main/.github/workflows "This path skips through empty directories")

 | 

[.github/ workflows](/vercel-labs/json-render/tree/main/.github/workflows "This path skips through empty directories")

 |  |  |
| 

[.husky](/vercel-labs/json-render/tree/main/.husky ".husky")

 | 

[.husky](/vercel-labs/json-render/tree/main/.husky ".husky")

 | 

[format](/vercel-labs/json-render/commit/ec751154615d22ad210e289c4903b2e8ee258f7f "format")

 |  |
| 

[.vscode](/vercel-labs/json-render/tree/main/.vscode ".vscode")

 | 

[.vscode](/vercel-labs/json-render/tree/main/.vscode ".vscode")

 | 

[mcp (](/vercel-labs/json-render/commit/1cc87310c90d65ff2c93a97b58acd91d231c2e0f "mcp (#184)
* mcp
* fix lint")[#184](https://github.com/vercel-labs/json-render/pull/184)[)](/vercel-labs/json-render/commit/1cc87310c90d65ff2c93a97b58acd91d231c2e0f "mcp (#184)
* mcp
* fix lint")

 |  |
| 

[apps/ web](/vercel-labs/json-render/tree/main/apps/web "This path skips through empty directories")

 | 

[apps/ web](/vercel-labs/json-render/tree/main/apps/web "This path skips through empty directories")

 |  |  |
| 

[examples](/vercel-labs/json-render/tree/main/examples "examples")

 | 

[examples](/vercel-labs/json-render/tree/main/examples "examples")

 |  |  |
| 

[packages](/vercel-labs/json-render/tree/main/packages "packages")

 | 

[packages](/vercel-labs/json-render/tree/main/packages "packages")

 |  |  |
| 

[scripts](/vercel-labs/json-render/tree/main/scripts "scripts")

 | 

[scripts](/vercel-labs/json-render/tree/main/scripts "scripts")

 |  |  |
| 

[skills](/vercel-labs/json-render/tree/main/skills "skills")

 | 

[skills](/vercel-labs/json-render/tree/main/skills "skills")

 | 

[feat: add @json-render/ink terminal renderer (](/vercel-labs/json-render/commit/d69a59ea9d84d6667f6332eacd2549228a44278e "feat: add @json-render/ink terminal renderer (#240)
* feat: add @json-render/ink terminal renderer and ink-chat example
Adds a new `@json-render/ink` package that brings json-render specs to
terminal UIs via Ink (React for CLIs). Includes 24 standard components
(layout, text, inputs, markdown, etc.), context providers for state,
validation, visibility, actions, focus, and repeat scopes, plus a
streaming JSONL hook for progressive spec rendering.
Also adds an `ink-chat` example app demonstrating an AI chat interface
in the terminal with streaming responses, tool calls, and interactive
wizard flows.
Includes 76 tests (24 unit + 52 e2e), docs page, and web app integration.
* feat: show live spec preview during streaming
Render the spec progressively as JSONL patches arrive instead of only
showing a spinner. The preview disappears when streaming completes and
the finalized message replaces it in history.
* feat: clip streaming preview to 6 lines
* refactor: move spinner into input box, show full streaming preview
* fix: skip spacer during streaming to prevent clipping tall previews
* fix: strip invisible colors on dark terminal backgrounds
Drop foreground colors like "black" and "#000000" from AI-generated
specs so text remains readable on dark terminals. Removed hardcoded
color="black" from Badge and added safeColor() guard to all components
that accept user-specified color props.
* fix: always show spacer to keep input pinned to bottom
* fix: show dash placeholder for empty values in Table and KeyValue
Empty or null values in Table cells and KeyValue now render as "—"
instead of blank space. Also removed dimColor from ListItem subtitle
and trailing for better readability on dark terminals.
* fix: division by zero in Sparkline sampling when maxWidth is 1
* fix: Review feedback
Signed-off-by: Alexis Rico <sferadev@gmail.com>
* fix: Update readme
Signed-off-by: Alexis Rico <sferadev@gmail.com>
---------
Signed-off-by: Alexis Rico <sferadev@gmail.com>")[#240](https://github.com/vercel-labs/json-render/pull/240)[)](/vercel-labs/json-render/commit/d69a59ea9d84d6667f6332eacd2549228a44278e "feat: add @json-render/ink terminal renderer (#240)
* feat: add @json-render/ink terminal renderer and ink-chat example
Adds a new `@json-render/ink` package that brings json-render specs to
terminal UIs via Ink (React for CLIs). Includes 24 standard components
(layout, text, inputs, markdown, etc.), context providers for state,
validation, visibility, actions, focus, and repeat scopes, plus a
streaming JSONL hook for progressive spec rendering.
Also adds an `ink-chat` example app demonstrating an AI chat interface
in the terminal with streaming responses, tool calls, and interactive
wizard flows.
Includes 76 tests (24 unit + 52 e2e), docs page, and web app integration.
* feat: show live spec preview during streaming
Render the spec progressively as JSONL patches arrive instead of only
showing a spinner. The preview disappears when streaming completes and
the finalized message replaces it in history.
* feat: clip streaming preview to 6 lines
* refactor: move spinner into input box, show full streaming preview
* fix: skip spacer during streaming to prevent clipping tall previews
* fix: strip invisible colors on dark terminal backgrounds
Drop foreground colors like "black" and "#000000" from AI-generated
specs so text remains readable on dark terminals. Removed hardcoded
color="black" from Badge and added safeColor() guard to all components
that accept user-specified color props.
* fix: always show spacer to keep input pinned to bottom
* fix: show dash placeholder for empty values in Table and KeyValue
Empty or null values in Table cells and KeyValue now render as "—"
instead of blank space. Also removed dimColor from ListItem subtitle
and trailing for better readability on dark terminals.
* fix: division by zero in Sparkline sampling when maxWidth is 1
* fix: Review feedback
Signed-off-by: Alexis Rico <sferadev@gmail.com>
* fix: Update readme
Signed-off-by: Alexis Rico <sferadev@gmail.com>
---------
Signed-off-by: Alexis Rico <sferadev@gmail.com>")

 |  |
|  |

## json-render

**The Generative UI framework.**

Generate dynamic, personalized UIs from prompts without sacrificing reliability. Predefined components and actions for safe, predictable output.

```
# for React
npm install @json-render/core @json-render/react
# for React with pre-built shadcn/ui components
npm install @json-render/shadcn
# or for React Native
npm install @json-render/core @json-render/react-native
# or for video
npm install @json-render/core @json-render/remotion
# or for PDF documents
npm install @json-render/core @json-render/react-pdf
# or for HTML email
npm install @json-render/core @json-render/react-email @react-email/components @react-email/render
# or for Vue
npm install @json-render/core @json-render/vue
# or for Svelte
npm install @json-render/core @json-render/svelte
# or for SolidJS
npm install @json-render/core @json-render/solid
# or for terminal UIs
npm install @json-render/core @json-render/ink ink react
# or for 3D scenes
npm install @json-render/core @json-render/react-three-fiber @react-three/fiber @react-three/drei three
```

## Why json-render?

json-render is a **Generative UI** framework: AI generates interfaces from natural language prompts, constrained to components you define. You set the guardrails, AI generates within them:

- **Guardrailed** - AI can only use components in your catalog
- **Predictable** - JSON output matches your schema, every time
- **Fast** - Stream and render progressively as the model responds
- **Cross-Platform** - React, Vue, Svelte, Solid (web), React Native (mobile) from the same catalog
- **Batteries Included** - 36 pre-built shadcn/ui components ready to use

## Quick Start

```
import { defineCatalog } from "@json-render/core";
import { schema } from "@json-render/react/schema";
import { z } from "zod";

const catalog = defineCatalog(schema, {
  components: {
 Card: {
 props: z.object({ title: z.string() }),
 description: "A card container",
 },
 Metric: {
 props: z.object({
 label: z.string(),
 value: z.string(),
 format: z.enum(["currency", "percent", "number"]).nullable(),
 }),
 description: "Display a metric value",
 },
 Button: {
 props: z.object({
 label: z.string(),
 action: z.string(),
 }),
 description: "Clickable button",
 },
  },
  actions: {
 export_report: { description: "Export dashboard to PDF" },
 refresh_data: { description: "Refresh all metrics" },
  },
});
```

```
import { defineRegistry, Renderer } from "@json-render/react";

const { registry } = defineRegistry(catalog, {
  components: {
 Card: ({ props, children }) => (
 <div className="card">
 <h3>{props.title}</h3>
 {children}
 </div>
 ),
 Metric: ({ props }) => (
 <div className="metric">
 <span>{props.label}</span>
 <span>{format(props.value, props.format)}</span>
 </div>
 ),
 Button: ({ props, emit }) => (
 <button onClick={() => emit("press")}>{props.label}</button>
 ),
  },
});
```

```
function Dashboard({ spec }) {
  return <Renderer spec={spec} registry={registry} />;
}
```

**That's it.** AI generates JSON, you render it safely.

* * *

## Packages

| Package | Description |
| --- | --- |
| `@json-render/core` | Schemas, catalogs, AI prompts, dynamic props, SpecStream utilities |
| `@json-render/react` | React renderer, contexts, hooks |
| `@json-render/vue` | Vue 3 renderer, composables, providers |
| `@json-render/svelte` | Svelte 5 renderer with runes-based reactivity |
| `@json-render/solid` | SolidJS renderer with fine-grained reactive contexts |
| `@json-render/shadcn` | 36 pre-built shadcn/ui components (Radix UI + Tailwind CSS) |
| `@json-render/react-three-fiber` | React Three Fiber renderer for 3D scenes (19 built-in components) |
| `@json-render/react-native` | React Native renderer with standard mobile components |
| `@json-render/remotion` | Remotion video renderer, timeline schema |
| `@json-render/react-pdf` | React PDF renderer for generating PDF documents from specs |
| `@json-render/react-email` | React Email renderer for HTML/plain-text emails from specs |
| `@json-render/ink` | Ink terminal renderer with built-in components for interactive TUIs. |
| `@json-render/image` | Image renderer for SVG/PNG output (OG images, social cards) via Satori |
| `@json-render/codegen` | Utilities for generating code from json-render UI trees |
| `@json-render/redux` | Redux / Redux Toolkit adapter for `StateStore` |
| `@json-render/zustand` | Zustand adapter for `StateStore` |
| `@json-render/jotai` | Jotai adapter for `StateStore` |
| `@json-render/xstate` | XState Store (atom) adapter for `StateStore` |
| `@json-render/mcp` | MCP Apps integration for Claude, ChatGPT, Cursor, VS Code |
| `@json-render/yaml` | YAML wire format with streaming parser, edit modes, AI SDK transform |

## Renderers

### React (UI)

```
import { defineRegistry, Renderer } from "@json-render/react";
import { schema } from "@json-render/react/schema";

// Flat spec format (root key + elements map)
const spec = {
  root: "card-1",
  elements: {
 "card-1": {
 type: "Card",
 props: { title: "Hello" },
 children: ["button-1"],
 },
 "button-1": {
 type: "Button",
 props: { label: "Click me" },
 children: [],
 },
  },
};

// defineRegistry creates a type-safe component registry
const { registry } = defineRegistry(catalog, { components });
<Renderer spec={spec} registry={registry} />;
```

### Vue (UI)

```
import { h } from "vue";
import { defineRegistry, Renderer } from "@json-render/vue";
import { schema } from "@json-render/vue/schema";

const { registry } = defineRegistry(catalog, {
  components: {
 Card: ({ props, children }) =>
 h("div", { class: "card" }, [h("h3", null, props.title), children]),
 Button: ({ props, emit }) =>
 h("button", { onClick: () => emit("press") }, props.label),
  },
});

// In your Vue component template:
// <Renderer :spec="spec" :registry="registry" />
```

### Svelte (UI)

```
import { defineRegistry, Renderer } from "@json-render/svelte";
import { schema } from "@json-render/svelte/schema";

const { registry } = defineRegistry(catalog, {
  components: {
 Card: ({ props, children }) => /* Svelte 5 snippet */,
 Button: ({ props, emit }) => /* Svelte 5 snippet */,
  },
});

// In your Svelte component:
// <Renderer spec={spec} registry={registry} />
```

### Solid (UI)

```
import { defineRegistry, Renderer } from "@json-render/solid";
import { schema } from "@json-render/solid/schema";

const { registry } = defineRegistry(catalog, {
  components: {
 Card: (renderProps) => <div>{renderProps.children}</div>,
 Button: (renderProps) => (
 <button onClick={() => renderProps.emit("press")}>
 {renderProps.element.props.label as string}
 </button>
 ),
  },
});

<Renderer spec={spec} registry={registry} />;
```

### shadcn/ui (Web)

```
import { defineCatalog } from "@json-render/core";
import { schema } from "@json-render/react/schema";
import { defineRegistry, Renderer } from "@json-render/react";
import { shadcnComponentDefinitions } from "@json-render/shadcn/catalog";
import { shadcnComponents } from "@json-render/shadcn";

// Pick components from the 36 standard definitions
const catalog = defineCatalog(schema, {
  components: {
 Card: shadcnComponentDefinitions.Card,
 Stack: shadcnComponentDefinitions.Stack,
 Heading: shadcnComponentDefinitions.Heading,
 Button: shadcnComponentDefinitions.Button,
  },
  actions: {},
});

// Use matching implementations
const { registry } = defineRegistry(catalog, {
  components: {
 Card: shadcnComponents.Card,
 Stack: shadcnComponents.Stack,
 Heading: shadcnComponents.Heading,
 Button: shadcnComponents.Button,
  },
});

<Renderer spec={spec} registry={registry} />;
```

```
import { defineCatalog } from "@json-render/core";
import { schema } from "@json-render/react-native/schema";
import {
  standardComponentDefinitions,
  standardActionDefinitions,
} from "@json-render/react-native/catalog";
import { defineRegistry, Renderer } from "@json-render/react-native";

// 25+ standard components included
const catalog = defineCatalog(schema, {
  components: { ...standardComponentDefinitions },
  actions: standardActionDefinitions,
});

const { registry } = defineRegistry(catalog, { components: {} });
<Renderer spec={spec} registry={registry} />;
```

### Remotion (Video)

```
import { Player } from "@remotion/player";
import {
  Renderer,
  schema,
  standardComponentDefinitions,
} from "@json-render/remotion";

// Timeline spec format
const spec = {
  composition: {
 id: "video",
 fps: 30,
 width: 1920,
 height: 1080,
 durationInFrames: 300,
  },
  tracks: [{ id: "main", name: "Main", type: "video", enabled: true }],
  clips: [
 {
 id: "clip-1",
 trackId: "main",
 component: "TitleCard",
 props: { title: "Hello" },
 from: 0,
 durationInFrames: 90,
 },
  ],
  audio: { tracks: [] },
};

<Player
  component={Renderer}
  inputProps={{ spec }}
  durationInFrames={spec.composition.durationInFrames}
  fps={spec.composition.fps}
  compositionWidth={spec.composition.width}
  compositionHeight={spec.composition.height}
/>;
```

```
import { renderToBuffer } from "@json-render/react-pdf";

const spec = {
  root: "doc",
  elements: {
 doc: {
 type: "Document",
 props: { title: "Invoice" },
 children: ["page-1"],
 },
 "page-1": {
 type: "Page",
 props: { size: "A4" },
 children: ["heading-1", "table-1"],
 },
 "heading-1": {
 type: "Heading",
 props: { text: "Invoice #1234", level: "h1" },
 children: [],
 },
 "table-1": {
 type: "Table",
 props: {
 columns: [
 { header: "Item", width: "60%" },
 { header: "Price", width: "40%", align: "right" },
 ],
 rows: [
 ["Widget A", "$10.00"],
 ["Widget B", "$25.00"],
 ],
 },
 children: [],
 },
  },
};

// Render to buffer, stream, or file
const buffer = await renderToBuffer(spec);
```

```
import { renderToHtml } from "@json-render/react-email";
import { schema, standardComponentDefinitions } from "@json-render/react-email";
import { defineCatalog } from "@json-render/core";

const catalog = defineCatalog(schema, {
  components: standardComponentDefinitions,
});

const spec = {
  root: "html-1",
  elements: {
 "html-1": {
 type: "Html",
 props: { lang: "en", dir: "ltr" },
 children: ["head-1", "body-1"],
 },
 "head-1": { type: "Head", props: {}, children: [] },
 "body-1": {
 type: "Body",
 props: { style: { backgroundColor: "#f6f9fc" } },
 children: ["container-1"],
 },
 "container-1": {
 type: "Container",
 props: {
 style: { maxWidth: "600px", margin: "0 auto", padding: "20px" },
 },
 children: ["heading-1", "text-1"],
 },
 "heading-1": { type: "Heading", props: { text: "Welcome" }, children: [] },
 "text-1": {
 type: "Text",
 props: { text: "Thanks for signing up." },
 children: [],
 },
  },
};

const html = await renderToHtml(spec);
```

### Image (SVG/PNG)

```
import { renderToPng } from "@json-render/image/render";

const spec = {
  root: "frame",
  elements: {
 frame: {
 type: "Frame",
 props: { width: 1200, height: 630, backgroundColor: "#1a1a2e" },
 children: ["heading"],
 },
 heading: {
 type: "Heading",
 props: { text: "Hello World", level: "h1", color: "#ffffff" },
 children: [],
 },
  },
};

// Render to PNG (requires @resvg/resvg-js)
const png = await renderToPng(spec, { fonts });

// Or render to SVG string
import { renderToSvg } from "@json-render/image/render";
const svg = await renderToSvg(spec, { fonts });
```

### Three.js (3D)

```
import { defineCatalog } from "@json-render/core";
import { schema, defineRegistry } from "@json-render/react";
import {
  threeComponentDefinitions,
  threeComponents,
  ThreeCanvas,
} from "@json-render/react-three-fiber";

const catalog = defineCatalog(schema, {
  components: {
 Box: threeComponentDefinitions.Box,
 Sphere: threeComponentDefinitions.Sphere,
 AmbientLight: threeComponentDefinitions.AmbientLight,
 DirectionalLight: threeComponentDefinitions.DirectionalLight,
 OrbitControls: threeComponentDefinitions.OrbitControls,
  },
  actions: {},
});

const { registry } = defineRegistry(catalog, {
  components: {
 Box: threeComponents.Box,
 Sphere: threeComponents.Sphere,
 AmbientLight: threeComponents.AmbientLight,
 DirectionalLight: threeComponents.DirectionalLight,
 OrbitControls: threeComponents.OrbitControls,
  },
});

<ThreeCanvas
  spec={spec}
  registry={registry}
  shadows
  camera={{ position: [5, 5, 5], fov: 50 }}
  style={{ width: "100%", height: "100vh" }}
/>;
```

### Ink (Terminal)

```
import { defineCatalog } from "@json-render/core";
import {
  schema,
  standardComponentDefinitions,
  standardActionDefinitions,
  defineRegistry,
  Renderer,
  JSONUIProvider,
} from "@json-render/ink";

const catalog = defineCatalog(schema, {
  components: { ...standardComponentDefinitions },
  actions: standardActionDefinitions,
});

const { registry } = defineRegistry(catalog, { components: {} });

const spec = {
  root: "card-1",
  elements: {
 "card-1": {
 type: "Card",
 props: { title: "Status" },
 children: ["status-1"],
 },
 "status-1": {
 type: "StatusLine",
 props: { label: "Build", status: "success" },
 children: [],
 },
  },
};

<JSONUIProvider initialState={{}}>
  <Renderer spec={spec} registry={registry} />
</JSONUIProvider>;
```

## Features

### Streaming (SpecStream)

Stream AI responses progressively:

```
import { createSpecStreamCompiler } from "@json-render/core";

const compiler = createSpecStreamCompiler<MySpec>();

// Process chunks as they arrive
const { result, newPatches } = compiler.push(chunk);
setSpec(result); // Update UI with partial result

// Get final result
const finalSpec = compiler.getResult();
```

Generate system prompts from your catalog:

```
const systemPrompt = catalog.prompt();
// Includes component descriptions, props schemas, available actions
```

### Conditional Visibility

```
{
  "type": "Alert",
  "props": { "message": "Error occurred" },
  "visible": [
 { "$state": "/form/hasError" },
 { "$state": "/form/errorDismissed", "not": true }
  ]
}
```

### Dynamic Props

Any prop value can be data-driven using expressions:

```
{
  "type": "Icon",
  "props": {
 "name": {
 "$cond": { "$state": "/activeTab", "eq": "home" },
 "$then": "home",
 "$else": "home-outline"
 },
 "color": {
 "$cond": { "$state": "/activeTab", "eq": "home" },
 "$then": "#007AFF",
 "$else": "#8E8E93"
 }
  }
}
```

Expression forms:

- **`{ "$state": "/state/key" }`** - reads a value from the state model
- **`{ "$cond": <condition>, "$then": <value>, "$else": <value> }`** - evaluates a condition and picks a branch
- **`{ "$template": "Hello, ${/user/name}!" }`** - interpolates state values into strings
- **`{ "$computed": "fn", "args": { ... } }`** - calls a registered function with resolved args

### Actions

Components can trigger actions, including the built-in `setState` action:

```
{
  "type": "Pressable",
  "props": {
 "action": "setState",
 "actionParams": { "statePath": "/activeTab", "value": "home" }
  },
  "children": ["home-icon"]
}
```

The `setState` action updates the state model directly, which re-evaluates visibility conditions and dynamic prop expressions.

### State Watchers

React to state changes by triggering actions:

```
{
  "type": "Select",
  "props": {
 "value": { "$bindState": "/form/country" },
 "options": ["US", "Canada", "UK"]
  },
  "watch": {
 "/form/country": {
 "action": "loadCities",
 "params": { "country": { "$state": "/form/country" } }
 }
  }
}
```

`watch` is a top-level field on elements (sibling of `type` / `props` / `children`). Watchers fire when the watched value changes, not on initial render.

* * *

## Demo

```
git clone https://github.com/vercel-labs/json-render
cd json-render
pnpm install
pnpm dev
```

- [http://json-render.localhost:1355](http://json-render.localhost:1355) - Docs & Playground
- [http://dashboard-demo.json-render.localhost:1355](http://dashboard-demo.json-render.localhost:1355) - Example Dashboard
- [http://react-email-demo.json-render.localhost:1355](http://react-email-demo.json-render.localhost:1355) - React Email Example
- [http://remotion-demo.json-render.localhost:1355](http://remotion-demo.json-render.localhost:1355) - Remotion Video Example
- Chat Example: run `pnpm dev` in `examples/chat`
- Svelte Example: run `pnpm dev` in `examples/svelte` or `examples/svelte-chat`
- Vue Example: run `pnpm dev` in `examples/vue`
- Vite Renderers (React + Vue + Svelte + Solid): run `pnpm dev` in `examples/vite-renderers`
- React Native example: run `npx expo start` in `examples/react-native`

```
flowchart LR
 A[User Prompt] --> B[AI + Catalog]
 B --> C[JSON Spec]
 C --> D[Renderer]

 B -.- E([guardrailed])
 C -.- F([predictable])
 D -.- G([streamed])
```

1.  **Define the guardrails** - what components, actions, and data bindings AI can use
2.  **Prompt** - describe what you want in natural language
3.  **AI generates JSON** - output is always predictable, constrained to your catalog
4.  **Render fast** - stream and render progressively as the model responds

## License

Apache-2.0

## Releases 205

[\+ 204 releases](/vercel-labs/json-render/releases)

## Packages

No packages published

## Languages

- [TypeScript 80.4%](/vercel-labs/json-render/search?l=typescript)
- [MDX 12.3%](/vercel-labs/json-render/search?l=mdx)
- [Svelte 6.3%](/vercel-labs/json-render/search?l=svelte)
- Other 1.0%

* * *

# Reverse-engineering Claude's generative UI - then building it for the terminal

https://michaellivs.com/blog/reverse-engineering-claude-generative-ui/

/ Article

![SaaS dashboard widget rendered in a native macOS window](/images/generative-ui/dashboard.gif)

```bash
pi install npm:pi-generative-ui
```

Source: [github.com/Michaelliv/pi-generative-ui](https://github.com/Michaelliv/pi-generative-ui)

## The Discovery

Anthropic [announced generative UI for Claude](https://x.com/claudeai/status/2032124273587077133) a couple of hours ago. Interactive widgets - sliders, charts, animations - rendered inline in claude.ai conversations. Not images. Not code blocks. Living HTML applications with JavaScript running inside the chat.

This wasn’t a surprise. Generative UI has been pushed by Vercel and others for a while, and I knew Anthropic would do something with it. This also isn’t the first time I’ve dug into Anthropic’s implementation details - I’ve previously [reverse-engineered their sandbox architecture](/blog/sandboxed-execution-environment) and written about their [sandbox](/blog/sandbox-comparison-2026).

So I went to claude.ai with a specific purpose: understand exactly how they implemented it. I ended up building my own version for [pi](https://github.com/badlogic/pi-mono), the terminal-based coding agent.

* * *

## Part 1: Interrogating Claude About Its Own UI

### The Tool, Not the Markdown

My first assumption was wrong. I thought Claude was outputting HTML as part of its markdown response and the frontend was rendering it inline. Claude corrected me:

> “Ha, yes! Caught me - it’s not ‘part of the markdown output’ at all. I call a tool called `show_widget` and pass the HTML as a parameter.”

So it’s a **tool call**. The same mechanism as web search or file operations. The HTML is a parameter payload, not streamed text. Here’s the shape Claude described:

```json
{

  "i_have_seen_read_me": true,

  "title": "snake_case_identifier",

  "loading_messages": ["First loading message", "Second loading message"],

  "widget_code": "...styles...\n...html content...\n..."

}
```

Four parameters:

- **`i_have_seen_read_me`** - A boolean forcing function. Claude must call a `read_me` tool first to load design guidelines before it can use `show_widget`. It’s a compile-time check for documentation compliance.
- **`title`** - A snake\_case identifier for the widget.
- **`loading_messages`** - 1-4 short strings shown while the widget renders (the “Spinning up particles…” messages you see before content appears).
- **`widget_code`** - Raw HTML fragment. No `<!DOCTYPE>`, no `<html>`, no `<head>`, no `<body>`. Just content.

Before Claude can call `show_widget`, it must call `read_me` with a `modules` parameter:

```json
{

  "modules": ["interactive", "chart"]

}
```

Available modules: `diagram`, `mockup`, `interactive`, `chart`, `art`.

Each module returns different design guidelines - the `chart` module gives Chart.js patterns, `art` gives illustration rules, `mockup` gives UI component tokens. Claude described it perfectly:

> “It’s a lazy documentation system - instead of dumping the entire design system into my context upfront (which would be expensive tokens on every message), it loads only the relevant subset on demand.”

This is **progressive disclosure applied to the model’s own instructions**. The base system prompt stays lean; specialized knowledge loads on-demand when the task requires it.

### Not an Iframe - Live DOM Injection

I noticed the widget rendered **live** as Claude streamed its response. The sliders and cards appeared before Claude finished generating the `widget_code` parameter. That’s not how iframes work - an iframe would need the complete HTML before rendering.

Claude initially claimed it was a sandboxed iframe, but I pushed back:

> “It renders live on my screen, meaning that it somehow handles partial rendering of the HTML. It’s not a sandbox.”

Claude’s revised analysis:

> “The streaming behavior gives it away completely. If it were a sandboxed iframe, it would have to wait for the complete HTML before rendering. But you’re seeing it render as tokens stream in. That’s only possible if it’s **direct DOM injection into the parent page**.”

The evidence:

- **CSS variables work** - `var(--color-text-primary)` resolves correctly because it’s the same document, same cascade
- **`sendPrompt()` works** - a function on the parent page, accessible to injected code
- **Background is transparent** - no iframe container, just nodes in the DOM
- **No loading flash** - no iframe border, no scrollbar, no white-background box

The “sandbox” is almost certainly just a **Content Security Policy** on the parent page restricting which CDN domains `script src` tags can load from:

- `cdnjs.cloudflare.com`
- `cdn.jsdelivr.net`
- `unpkg.com`
- `esm.sh`

### How It Differs from Artifacts

This was a key insight from the conversation:

|  | Artifacts | Visualizer (`show_widget`) |
| --- | --- | --- |
| **Purpose** | Deliverables - files you keep, download, share | Inline enhancements - part of the conversation flow |
| **Display** | Side panel with download button | Inline in the chat, transparent background |
| **Libraries** | Closed set of pre-bundled libraries | Any library from CDN allowlist, downloaded live |
| **Persistence** | Survives across sessions | Ephemeral, tied to the message |
| **Trigger** | ”Build me a calculator” (deliverable language) | “Show me how compound interest works” (explanatory language) |

The CDN point is crucial. Artifacts have a fixed set of available libraries. The visualizer downloads Chart.js, D3, Three.js - whatever it needs - live from CDNs. This is why the CSP allowlist exists: it’s the security boundary for arbitrary CDN fetches.

### The Streaming Architecture

Putting it all together, here’s how claude.ai renders generative UI:

1.  LLM starts generating the `show_widget` tool call
2.  The `widget_code` parameter streams token by token as JSON string chunks
3.  The client does incremental HTML parsing on the partial content
4.  DOM nodes are inserted into the page in real-time via `innerHTML` or similar
5.  CSS variables resolve immediately (same document)
6.  `style` blocks and HTML structure render as they arrive
7.  `script` tags execute once streaming completes (which is why scripts go last)
8.  CDN libraries load asynchronously; charts/interactivity activate after scripts run

This explains the design guideline that says “Structure code so useful content appears early: `style` (short) → content HTML → `script` last.” The content renders progressively; the scripts activate it at the end.

* * *

## Part 2: Building It for Pi

### The Problem

[Pi](https://github.com/badlogic/pi-mono) is a terminal-based coding agent (I’ve [compared every CLI coding agent](/blog/cli-coding-agents-compared) if you’re curious). Terminals render text and (in modern ones) inline images. There is **no way to render interactive HTML with JavaScript inside a terminal**. The moment you need a `<canvas>`, an `<input type="range">`, or Chart.js, you need a browser engine.

My initial options were:

1.  **Terminal image protocols** (Sixel, Kitty graphics) - render HTML to a screenshot, display inline. No interactivity.
2.  **Local web server + browser** - serve HTML on localhost, auto-open browser tab. Full interactivity but exits the terminal.
3.  **TUI approximation** - parse HTML, render a simplified text version. Extremely limited.

None of these matched the claude.ai experience.

### Enter Glimpse

Then I found [Glimpse](https://github.com/hazat/glimpse) - a native macOS micro-UI library. It opens a WKWebView window in under 50ms via a tiny Swift binary with a Node.js wrapper. No Electron, no browser, no runtime dependencies.

Key capabilities:

- **Native WKWebView** - full browser engine (CSS, JS, Canvas, CDN libraries)
- **Sub-50ms startup** - feels instant
- **Bidirectional JSON** - `window.glimpse.send(data)` sends data from the page back to Node.js
- **Window modes** - floating, frameless, transparent, click-through, follow-cursor
- **`setHTML()`** - replace page content at runtime
- **`send(js)`** - evaluate JavaScript in the WebView

This was the missing piece. A real browser engine, spawnable from a pi extension, with bidirectional communication.

### The Extension Architecture

Pi extensions are TypeScript modules that can register custom tools, subscribe to lifecycle events, and render custom TUI components. The architecture:

```plaintext
LLM generates show_widget tool call

 │

 ▼

 ┌───────────────────┐

 │ message_update │──── streaming: intercept partial tool call JSON

 │ event │ extract widget_code, open Glimpse window early

 └────────┬──────────┘ feed partial HTML as tokens arrive

 │

 ▼

 ┌───────────────────┐

 │  tool_call │──── complete: final widget_code available

 │ event │

 └────────┬──────────┘

 │

 ▼

 ┌───────────────────┐

 │ execute() │──── reuse streaming window or open fresh

 │ │ wait for user interaction or window close

 └────────┬──────────┘ return interaction data as tool result

 │

 ▼

 ┌───────────────────┐

 │  renderCall │──── TUI: "show_widget compound interest 800×600"

 │  renderResult │──── TUI: "✓ compound interest 800×600"

 └───────────────────┘
```

### Two Tools, Mirroring Claude’s Pattern

**`visualize_read_me`** - Lazy documentation loader. Returns design guidelines by module (interactive, chart, mockup, art, diagram). The LLM calls this silently before its first widget, loading only the relevant guidelines into context.

```typescript
pi.registerTool({

  name: "visualize_read_me",

  label: "Read Guidelines",

  description: "Returns design guidelines for show_widget...",

  promptGuidelines: [

 "Call visualize_read_me once before your first show_widget call.",

 "Do NOT mention the read_me call to the user.",

  ],

  parameters: Type.Object({

 modules: Type.Array(StringEnum(AVAILABLE_MODULES)),

  }),

  async execute(_toolCallId, params) {

 return {

 content: [{ type: "text", text: getGuidelines(params.modules) }],

 details: { modules: params.modules },

 };

  },

});
```

**`show_widget`** - Takes HTML/SVG code, opens a native macOS window via Glimpse, returns user interaction data.

```typescript
pi.registerTool({

  name: "show_widget",

  label: "Show Widget",

  description: "Show visual content in a native macOS window...",

  parameters: Type.Object({

 i_have_seen_read_me: Type.Boolean(),

 title: Type.String(),

 widget_code: Type.String(),

 width: Type.Optional(Type.Number()),

 height: Type.Optional(Type.Number()),

 floating: Type.Optional(Type.Boolean()),

  }),

  async execute(_toolCallId, params, signal) {

 const { open } = await import(GLIMPSE_PATH);

 const win = open(wrapHTML(params.widget_code), {

 width: params.width ?? 800,

 height: params.height ?? 600,

 title: params.title.replace(/_/g, " "),

 });

 return new Promise((resolve) => {

 win.on("message", (data) => {

 resolve({ content: [{ type: "text", text: `User data: ${JSON.stringify(data)}` }] });

 });

 win.on("closed", () => {

 resolve({ content: [{ type: "text", text: "Window closed." }] });

 });

 });

  },

});
```

### Custom TUI Rendering

Pi extensions can provide `renderCall` and `renderResult` functions for custom terminal display. Instead of dumping raw HTML into the terminal, we show compact summaries:

```typescript
renderCall(args, theme) {

  const title = args.title.replace(/_/g, " ");

  return new Text(

 theme.fg("toolTitle", theme.bold("show_widget ")) +

 theme.fg("accent", title) +

 theme.fg("dim", ` ${args.width}×${args.height}`),

 0, 0

  );

},

renderResult(result, { isPartial, expanded }, theme) {

  if (isPartial) return new Text(theme.fg("warning", "⟳ Widget rendering..."), 0, 0);

  const details = result.details;

  let text = theme.fg("success", "✓ ") + theme.fg("accent", details.title);

  if (expanded && details.messageData) {

 text += "\n" + theme.fg("dim", `  Data: ${JSON.stringify(details.messageData)}`);

  }

  return new Text(text, 0, 0);

},
```

![Projectile motion simulator with planet selection](/images/generative-ui/simulator.gif)

* * *

## Part 3: The Streaming Challenge

### The Goal

On claude.ai, the widget renders progressively as tokens stream in. The HTML builds up visually - you see the styles apply, the structure form, cards and tables appear piece by piece, and then the chart pops in when the `script` executes at the end.

We wanted the same experience: the Glimpse window should open early and show content building up live.

### How Pi Streams Tool Calls

Pi’s AI layer (pi-ai) normalizes streaming events across all providers (Anthropic, OpenAI, Google, etc.) into a unified format:

```typescript
type AssistantMessageEvent =

  | { type: "toolcall_start"; contentIndex: number; partial: AssistantMessage }

  | { type: "toolcall_delta"; contentIndex: number; delta: string; partial: AssistantMessage }

  | { type: "toolcall_end"; contentIndex: number; toolCall: ToolCall; partial: AssistantMessage }
```

The key discovery: **pi-ai already parses partial JSON on every delta**. Looking at the Anthropic provider source:

```javascript
block.partialJson += event.delta.partial_json;

block.arguments = parseStreamingJson(block.partialJson);
```

So `partial.content[index].arguments` is a progressively-parsed object. On every `toolcall_delta`, we can read `arguments.widget_code` and get the HTML accumulated so far - no need for a partial JSON parser library.

We initially installed `partial-json` from npm before discovering this. Removed it immediately.

### Attempt 1: setHTML() on Every Delta

The first approach: listen to `message_update`, detect `show_widget` tool calls streaming, open a Glimpse window, and call `win.setHTML(wrappedHTML)` on every delta.

```typescript
pi.on("message_update", async (event) => {

  const raw = event.assistantMessageEvent;

  if (raw.type === "toolcall_delta" && streaming) {

 const block = raw.partial.content[raw.contentIndex];

 const html = block.arguments?.widget_code;

 if (html && html.length > 20) {

 streaming.window.setHTML(wrapHTML(html));

 }

  }

});
```

**Result**: It worked! The window opened and showed content building up. But it was **choppy as hell**. Every `setHTML()` call replaced the entire document - full page reflow, loss of scroll position, flash of unstyled content. Every 80ms, the entire page blinked.

### Attempt 2: Shell Page + innerHTML via JS Eval

Instead of replacing the entire document, we opened the window once with a shell HTML page containing an empty `<div id="root">`. Then we used `win.send()` (JavaScript evaluation in the WebView) to update just the innerHTML of that container:

```typescript
// Shell HTML loaded once - contains a <div id="root"> and a script

// that defines window._setContent(html) to update root's innerHTML

function shellHTML() {

  return `...

 <div id="root"></div>

 // _setContent: sets root.innerHTML to the provided html

  ...`;

}

// On each delta, eval JS to update content

streaming.window.send(`window._setContent('${escapeJS(html)}')`);
```

**Result**: Better - no full document replacement. But still choppy. `innerHTML` replaces all child nodes, so existing content gets destroyed and recreated on every update. There’s no visual continuity.

### Attempt 3: Naive DOM Appending

We tried tracking the previous content length and only appending new child nodes:

```typescript
window._setContent = function(html) {

  var root = document.getElementById('root');

  var tmp = document.createElement('div');

  tmp.innerHTML = html;

  // Only append nodes beyond what we already have

  for (var i = root.childNodes.length; i < tmp.childNodes.length; i++) {

 var node = tmp.childNodes[i].cloneNode(true);

 node.style.animation = '_fadeIn 0.3s ease both';

 root.appendChild(node);

  }

  // Update the last existing node (it was probably incomplete)

  // ...

};
```

**Result**: Elements appeared but **never faded in**. The problem: the browser auto-closes unclosed HTML tags when parsing partial content. `<div class="cards"><div class="c">` becomes:

```html
<div class="cards">

  <div class="c"></div>  <!-- browser auto-closed this -->

</div>
```

On the next update with more content, the tree structure changes fundamentally - it’s not “new nodes appended at the end,” it’s a completely different tree. The append logic couldn’t track what was actually new.

### Attempt 4: morphdom - DOM Diffing (The Solution)

We introduced [morphdom](https://github.com/patrick-steele-idem/morphdom), a fast DOM diffing library (used by frameworks like Marko). Instead of replacing innerHTML, morphdom compares the old and new DOM trees and applies **minimal patches** - updating changed nodes, adding new ones, leaving unchanged ones alone.

```typescript
function shellHTML() {

  // Returns a full HTML document with:

  // 1. A _fadeIn CSS animation (opacity 0→1, translateY 4px→0)

  // 2. morphdom loaded from cdn.jsdelivr.net

  // 3. A _setContent(html) function that:

  // - Buffers calls until morphdom loads (_morphReady flag)

  // - Creates a target div with the new HTML

  // - Calls morphdom(root, target) with callbacks:

  // onBeforeElUpdated: skip if from.isEqualNode(to)

  // onNodeAdded: apply _fadeIn animation to new elements

  return `...`;

}
```

The morphdom callbacks:

- **`onBeforeElUpdated`**: If the old node and new node are identical (`isEqualNode`), skip the update entirely. Existing content stays untouched in the DOM.
- **`onNodeAdded`**: When a genuinely new node appears in the tree, apply a CSS `_fadeIn` animation - 0.3s ease, subtle translateY for a “slide up” effect.

**Loading race condition**: morphdom loads asynchronously from CDN. If `_setContent` is called before it loads, the call silently does nothing. We solved this with a pending buffer:

```javascript
window._morphReady = false;

window._pending = null;

window._setContent = function(html) {

  if (!window._morphReady) { window._pending = html; return; }

  // ... morphdom diffing

};

// On morphdom load, flush:

onload="window._morphReady=true;

  if(window._pending){window._setContent(window._pending);window._pending=null;}"
```

### Script Execution

`innerHTML` doesn’t execute `script` tags. When the complete HTML arrives (on `toolcall_end`), we need to activate the scripts (Chart.js initialization, event listeners, etc.):

```javascript
window._runScripts = function() {

  document.querySelectorAll('#root script').forEach(function(old) {

 var s = document.createElement('script');

 if (old.src) { s.src = old.src; }

 else { s.textContent = old.textContent; }

 old.parentNode.replaceChild(s, old);

  });

};
```

This clones each `script` tag into a fresh element (which the browser will execute) and replaces the inert original.

### The Complete Streaming Flow

```plaintext
toolcall_start (show_widget detected)

  │

  ├── streaming state initialized

  │

  ▼

toolcall_delta (repeated, every ~token)

  │

  ├── read partial.content[index].arguments.widget_code

  ├── debounce 150ms

  ├── first time: open Glimpse window with shellHTML()

  │ └── morphdom loads from CDN in background

  ├── subsequent: win.send(`_setContent('${escapedHTML}')`)

  │ └── morphdom diffs old vs new DOM

  │ └── new nodes get _fadeIn animation

  │ └── unchanged nodes stay untouched

  │

  ▼

toolcall_end

  │

  ├── final _setContent with complete HTML

  ├── _runScripts() activates script tags

  │ └── Chart.js loads from CDN

  │ └── charts render

  │ └── event listeners attach

  │

  ▼

execute() called

  │

  ├── reuses existing streaming window (no double-open)

  ├── waits for:

  │ ├── window.glimpse.send(data) → user interaction

  │ ├── window close → user dismissed

  │ └── 120s timeout → auto-resolve

  ├── returns tool result with interaction data

  │

  ▼

TUI renders compact summary:

  "✓ compound interest 800×600"
```

### String Escaping

One subtle but critical detail: the HTML content is injected as a JavaScript string literal via `win.send()`. This means we need to escape:

```typescript
function escapeJS(s: string): string {

  return s

 .replace(/\\/g, '\\\\') // backslashes

 .replace(/'/g, "\\'") // single quotes (our string delimiter)

 .replace(/\n/g, '\\n') // newlines

 .replace(/\r/g, '\\r') // carriage returns

 .replace(/<\/script>/gi, '<\\/script>');  // closing script tags

}
```

The `<\/script>` replacement prevents the browser from interpreting a literal `/script` inside our JavaScript string as closing the outer script block.

![Architecture diagram streaming live](/images/generative-ui/diagram.gif)

* * *

## Part 4: Extracting the Design Guidelines - Verbatim

I opened the browser devtools, inspected the network requests, and found the full tool call payloads in the response bodies - including the complete `read_me` tool results containing Anthropic’s actual design guidelines.

The response JSON has this structure:

```json
{

  "chat_messages": [

 {

 "content": [

 {

 "type": "tool_use",

 "name": "visualize:read_me",

 "input": { "modules": ["interactive", "chart"] }

 },

 {

 "type": "tool_result",

 "name": "visualize:read_me",

 "content": [{ "type": "text", "text": "# Imagine - Visual Creation Suite\n\n## Modules\n..." }]

 }

 ]

 }

  ]

}
```

That `text` field in the `tool_result`? That’s the **complete design guidelines** that Anthropic feeds to Claude. Not a summary. Not Claude’s description of it. The actual system content, verbatim.

### Reconstructing the Module System

By triggering `read_me` with different module combinations across multiple messages, we extracted all 5 module responses:

| Modules requested | Response size | Unique sections included |
| --- | --- | --- |
| `["interactive"]` | 19K | Core + UI components + Color palette |
| `["chart"]` | 22K | Core + UI components + Color palette + Charts (Chart.js) |
| `["mockup"]` | 19K | Core + UI components + Color palette |
| `["art"]` | 17K | Core + SVG setup + Art and illustration |
| `["diagram"]` | 59K | Core + Color palette + SVG setup + Diagram types |

Every response shares the same **core** (philosophy, streaming rules, typography, CSS variables, `sendPrompt()` docs). Then each module appends its specific sections. Some sections are shared across modules - `UI components` appears in interactive, chart, and mockup; `SVG setup` appears in both art and diagram.

We wrote a script to:

1.  Parse the conversation JSON
2.  Split each `read_me` response at `##` heading boundaries
3.  Deduplicate shared sections
4.  Verify that recombining sections produces byte-identical output to the originals

The result: **10 unique sections** that can be recombined to reproduce any module response exactly (4/5 exact match, 1 has a single whitespace character difference).

### What’s Inside - The Design System

The guidelines are *thorough*. This isn’t a “use nice colors” pamphlet. It’s a production design system with hard rules:

[**Core**](https://github.com/Michaelliv/pi-generative-ui/blob/main/.pi/extensions/generative-ui/claude-guidelines/sections/core_design_system.md) - The foundation every widget must follow:

- Streaming-first architecture: `style` → HTML → `script` last
- No gradients, shadows, blur - they flash during streaming DOM diffs
- No `<!-- comments -->` - waste tokens and break streaming
- Two font weights only (400, 500) - never 600 or 700
- Sentence case everywhere, never Title Case or ALL CAPS
- CSS variables for all colors (`--color-text-primary`, `--color-background-secondary`)
- Dark mode is mandatory - every color must work in both modes
- CDN allowlist: `cdnjs.cloudflare.com`, `cdn.jsdelivr.net`, `unpkg.com`, `esm.sh`

[**Color palette**](https://github.com/Michaelliv/pi-generative-ui/blob/main/.pi/extensions/generative-ui/claude-guidelines/sections/color_palette.md) - Nine color ramps, each with 7 stops from lightest to darkest:

```plaintext
Purple: #EEEDFE → #CECBF6 → #AFA9EC → #7F77DD → #534AB7 → #3C3489 → #26215C

Teal: #E1F5EE → #9FE1CB → #5DCAA5 → #1D9E75 → #0F6E56 → #085041 → #04342C

Coral:  #FAECE7 → #F5C4B3 → #F0997B → #D85A30 → #993C1D → #712B13 → #4A1B0C

...
```

With strict rules: color encodes meaning, not sequence. 2-3 ramps per widget max. Text on colored backgrounds must use the 800/900 stop from the same ramp - never black.

[**SVG setup**](https://github.com/Michaelliv/pi-generative-ui/blob/main/.pi/extensions/generative-ui/claude-guidelines/sections/svg_setup.md) - A masterclass in SVG diagram engineering:

- ViewBox safety checklist (5 verification steps before finalizing)
- Font width calibration table with actual rendered pixel measurements
- Pre-built CSS classes (`c-blue`, `c-teal`, `t`, `ts`, `th`, `box`, `node`, `arr`)
- Arrow markers that auto-inherit stroke color via `context-stroke`
- Rules about `fill="none"` on connector paths (SVG defaults to `fill: black`)

[**Diagram types**](https://github.com/Michaelliv/pi-generative-ui/blob/main/.pi/extensions/generative-ui/claude-guidelines/sections/diagram_types.md) - The largest section by far:

- Two rules that “cause most diagram failures” (arrow intersection checks, box width from label length)
- Decision framework: route on the verb, not the noun (“how do LLMs work” → Illustrative, “transformer architecture” → Structural)
- Flowchart, structural, and illustrative diagram sub-specifications
- Complexity budgets: ≤5 words per subtitle, ≤4 boxes per horizontal tier

[**UI components**](https://github.com/Michaelliv/pi-generative-ui/blob/main/.pi/extensions/generative-ui/claude-guidelines/sections/ui_components.md) - Tokens for building mockups:

- Cards: white bg, 0.5px border, radius-lg, padding 1rem 1.25rem
- Buttons pre-styled with hover/active states
- Metric cards, form elements, skeleton loading patterns
- Layout rules for editorial vs card vs comparison views

[**Charts**](https://github.com/Michaelliv/pi-generative-ui/blob/main/.pi/extensions/generative-ui/claude-guidelines/sections/charts_chart_js.md) - Chart.js-specific guidance:

- Canvas wrapper sizing (`position: relative`, explicit height)
- Always disable default legend, build custom HTML legends
- Number formatting: `-$5M` not `$-5M`
- Dashboard layout patterns

### Using the Real Guidelines

We replaced our hand-written guidelines with the extracted originals. The `guidelines.ts` file is now verbatim Anthropic content, organized as lazy-loaded sections:

```typescript
export function getGuidelines(modules: string[]): string {

  let content = CORE;

  const seen = new Set<string>();

  for (const mod of modules) {

 const sections = MODULE_SECTIONS[mod];

 if (!sections) continue;

 for (const section of sections) {

 if (!seen.has(section)) {

 seen.add(section);

 content += "\n\n\n" + section;

 }

 }

  }

  return content + "\n";

}
```

The deduplication matters: if you request `["interactive", "chart"]`, the shared `UI components` and `Color palette` sections are included once, not twice. This matches exactly how claude.ai’s `read_me` tool behaves.

* * *

## Part 5: What We Learned

### 1\. Claude’s Generative UI is Simpler Than It Looks

It’s not a special rendering engine. It’s a tool call that returns HTML, injected into the DOM with incremental parsing as tokens stream. The sophistication is in the **design guidelines** - thousands of tokens of rules about colors, typography, dark mode, streaming-friendly structure, and when to use each pattern.

### 2\. The read\_me Pattern is Brilliant

Lazy-loading documentation into the model’s context on demand is a pattern worth stealing. Instead of a massive system prompt, you load specialized knowledge only when the task requires it. Our extension uses the same architecture: 5 modules, loaded selectively.

### 3\. DOM Diffing Solves Streaming Smoothness

You can’t just `innerHTML` on every token - it causes full-page flashes. You can’t naively append nodes - partial HTML parsing creates unpredictable tree structures. You need DOM diffing (morphdom, idiomorph, or similar) to apply minimal patches and animate only genuinely new nodes.

### 4\. Glimpse Makes Terminal Agents Visual

The terminal doesn’t need to render HTML. It needs to **spawn** something that renders HTML. Glimpse’s sub-50ms WKWebView windows with bidirectional JSON communication bridge the gap perfectly. The terminal stays a terminal; the visual content gets a real browser engine.

### 5\. pi-ai’s Normalized Streaming Events Are Gold

Pi’s AI layer normalizes streaming events across all providers into `toolcall_start` / `toolcall_delta` / `toolcall_end` with progressively-parsed `arguments`. This means the streaming approach works identically whether the model is Anthropic, OpenAI, Google, or any other provider. We didn’t need a partial JSON parser - pi-ai already does it.

* * *

## The Code

The complete extension is ~350 lines of TypeScript in two files:

- **`index.ts`** - Tool registration, streaming interception, Glimpse integration, TUI rendering
- **`guidelines.ts`** - Modular design guidelines (core + 5 lazy-loaded modules)

Dependencies:

- `glimpseui` - Native macOS WKWebView windows
- `morphdom` (CDN, loaded at runtime in the WebView) - DOM diffing for smooth streaming

The extension lives in `.pi/extensions/generative-ui/` and is auto-discovered by pi on startup. No configuration needed.

### Project Structure

```plaintext
pi-generative-ui/

├── .pi/

│ └── extensions/

│ └── generative-ui/

│ ├── index.ts # Extension entry point

│ └── guidelines.ts # Lazy-loaded design modules

├── node_modules/

│ └── glimpseui/ # Native macOS WKWebView

├── package.json

└── BLOG.md
```

* * *

## What’s Next

- **Dark mode adaptation** - Glimpse provides `appearance.darkMode` on the `ready` event. The shell could inject CSS variables matching the system appearance.
- **`sendPrompt()` equivalent** - claude.ai’s widgets have a `sendPrompt(text)` function that sends a message to the chat as if the user typed it. We could implement this via `window.glimpse.send({ type: 'prompt', text: '...' })` and have the extension call `pi.sendUserMessage()`.
- **Persistent widgets** - Keep a widget window open across multiple turns, pushing live updates from tool results.
- **Widget gallery** - Pre-built templates for common patterns (confirm dialogs, data tables, form wizards) that the LLM can reference by name.

* * *

## Acknowledgments

- **Claude** - for being surprisingly transparent about its own implementation when asked the right questions
- **Anthropic** - for the generative UI system that inspired this
- **[Glimpse](https://github.com/hazat/glimpse)** (Daniel Griesser) - the native macOS micro-UI that made this possible
- **[pi](https://github.com/badlogic/pi-mono)** (Mario Zechner) - the extensible coding agent that gave us the hooks to build on
- **[morphdom](https://github.com/patrick-steele-idem/morphdom)** - fast DOM diffing that solved the streaming smoothness problem

* * *

# CopilotKit/OpenGenerativeUI: Open-Source Generative UI Framework

https://github.com/CopilotKit/OpenGenerativeUI

[Open in github.dev](https://github.dev/) [Open in a new github.dev tab](https://github.dev/) [Open in codespace](/codespaces/new/CopilotKit/OpenGenerativeUI?resume=1)

| Name | Name | 
Last commit message

 | 

Last commit date

 |
| --- | --- | --- | --- |
| 

[Merge pull request](/CopilotKit/OpenGenerativeUI/commit/259e92c24c8ffaf9ba063ec1208e10b1f5998c4a) [#54](https://github.com/CopilotKit/OpenGenerativeUI/pull/54) [from CopilotKit/fix/native-python-agent](/CopilotKit/OpenGenerativeUI/commit/259e92c24c8ffaf9ba063ec1208e10b1f5998c4a)

[259e92c](/CopilotKit/OpenGenerativeUI/commit/259e92c24c8ffaf9ba063ec1208e10b1f5998c4a) ·

[82 Commits](/CopilotKit/OpenGenerativeUI/commits/main/)

 |
| 

[.chalk/ reviews/ sessions/ open-generative-ui](/CopilotKit/OpenGenerativeUI/tree/main/.chalk/reviews/sessions/open-generative-ui "This path skips through empty directories")

 | 

[.chalk/ reviews/ sessions/ open-generative-ui](/CopilotKit/OpenGenerativeUI/tree/main/.chalk/reviews/sessions/open-generative-ui "This path skips through empty directories")

 | 

[Add demo video to README, add status column to review findings](/CopilotKit/OpenGenerativeUI/commit/2533482b15962113db430976eaa5a09168c8c57b "Add demo video to README, add status column to review findings
Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>")

 |  |
| 

[.github/ workflows](/CopilotKit/OpenGenerativeUI/tree/main/.github/workflows "This path skips through empty directories")

 | 

[.github/ workflows](/CopilotKit/OpenGenerativeUI/tree/main/.github/workflows "This path skips through empty directories")

 | 

[fix: remove Python/uv from CI and fix smoke test SIGTERM failure](/CopilotKit/OpenGenerativeUI/commit/70f9184ae32afa4cda880af01d3563f85d83a1cc "fix: remove Python/uv from CI and fix smoke test SIGTERM failure
The agent is no longer a pnpm workspace member, so setup-python and
setup-uv are unnecessary in CI. Their post-job cache step failed because
uv never ran. Also drop Python from the smoke matrix (8→4 jobs) and
add `wait` after killing the frontend process to suppress the SIGTERM
exit code that was failing the smoke step.")

 |  |
| 

[apps](/CopilotKit/OpenGenerativeUI/tree/main/apps "apps")

 | 

[apps](/CopilotKit/OpenGenerativeUI/tree/main/apps "apps")

 | 

[fix: remove agent from pnpm workspace to fix Render build](/CopilotKit/OpenGenerativeUI/commit/f64850d638d07f81e0e6bf6595fe72ae2f406b05 "fix: remove agent from pnpm workspace to fix Render build
The agent's package.json made it a pnpm workspace member, so
pnpm install on the Node frontend service triggered "uv sync" in an
environment where uv doesn't exist — breaking Render deploys.
Remove apps/agent/package.json entirely (matching the Shadify pattern)
and run the agent dev server via a direct shell command in the root
package.json instead of through Turbo.")

 |  |
| 

[docker](/CopilotKit/OpenGenerativeUI/tree/main/docker "docker")

 | 

[docker](/CopilotKit/OpenGenerativeUI/tree/main/docker "docker")

 | 

[fix: replace langgraph-api Docker image with native FastAPI server](/CopilotKit/OpenGenerativeUI/commit/9b0694b9dc28c52566fca9beead76361a66ffdda "fix: replace langgraph-api Docker image with native FastAPI server
The langgraph-api Docker image requires PostgreSQL (DATABASE_URI) which
blocked Render deployment. Switch to serving the agent directly via
FastAPI + ag_ui_langgraph, matching the Shadify reference pattern.
- Replace Dockerfile.agent with native Python runtime on Render
- Add BoundedMemorySaver for memory-safe checkpointing (200 thread cap)
- Switch frontend from LangGraphAgent to LangGraphHttpAgent (AG-UI protocol)
- Remove langgraph-api, langgraph-cli deps (-25 packages)
Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>")

 |  |
| 

[.dockerignore](/CopilotKit/OpenGenerativeUI/blob/main/.dockerignore ".dockerignore")

 | 

[.dockerignore](/CopilotKit/OpenGenerativeUI/blob/main/.dockerignore ".dockerignore")

 | 

[feat: Open Generative UI with CopilotKit + LangGraph](/CopilotKit/OpenGenerativeUI/commit/50d90b3310e275e3aabb6579c78dd5264374487f "feat: Open Generative UI with CopilotKit + LangGraph")

 |  |
| 

[.env.example](/CopilotKit/OpenGenerativeUI/blob/main/.env.example ".env.example")

 | 

[.env.example](/CopilotKit/OpenGenerativeUI/blob/main/.env.example ".env.example")

 | 

[fix: feature-flag in-memory rate limiter, disable by default](/CopilotKit/OpenGenerativeUI/commit/e45e254f993a3017529be2b5483b048ec1b89e85 "fix: feature-flag in-memory rate limiter, disable by default
In-memory rate limiting doesn't scale across multiple instances for
high-traffic deployments. Disable by default via RATE_LIMIT_ENABLED
env var so it doesn't silently misbehave at scale. Can be re-enabled
for single-instance or low-traffic deployments.")

 |  |
| 

[.gitignore](/CopilotKit/OpenGenerativeUI/blob/main/.gitignore ".gitignore")

 | 

[.gitignore](/CopilotKit/OpenGenerativeUI/blob/main/.gitignore ".gitignore")

 | 

[feat: add Render deployment blueprint and prepare for production](/CopilotKit/OpenGenerativeUI/commit/b811fa17aa9d3a6af801e116467bf4878463b9d0 "feat: add Render deployment blueprint and prepare for production
Add render.yaml with two services: a public Docker-based Next.js
frontend and a private Python LangGraph agent. Normalize the
LANGGRAPH_DEPLOYMENT_URL to handle Render's bare host:port format,
and make MCP server configuration opt-in via env var instead of
hardcoding the excalidraw default.
Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>")

 |  |
| 

[CLAUDE.md](/CopilotKit/OpenGenerativeUI/blob/main/CLAUDE.md "CLAUDE.md")

 | 

[CLAUDE.md](/CopilotKit/OpenGenerativeUI/blob/main/CLAUDE.md "CLAUDE.md")

 | 

[feat: Open Generative UI with CopilotKit + LangGraph](/CopilotKit/OpenGenerativeUI/commit/50d90b3310e275e3aabb6579c78dd5264374487f "feat: Open Generative UI with CopilotKit + LangGraph")

 |  |
| 

[CODE\_OF\_CONDUCT.md](/CopilotKit/OpenGenerativeUI/blob/main/CODE_OF_CONDUCT.md "CODE_OF_CONDUCT.md")

 | 

[CODE\_OF\_CONDUCT.md](/CopilotKit/OpenGenerativeUI/blob/main/CODE_OF_CONDUCT.md "CODE_OF_CONDUCT.md")

 | 

[docs: add Makefile, update README with run commands, fix community refs](/CopilotKit/OpenGenerativeUI/commit/ae44dd4a61f50c63141f873a4dfc7a912aa11cc0 "docs: add Makefile, update README with run commands, fix community refs
- Add Makefile with setup, dev, build, lint, and clean targets
- Update README Quick Start to use make commands with full command table
- Update CONTRIBUTING.md dev setup to reference Makefile
- Fix CODE_OF_CONDUCT.md to reference CopilotKit community consistently")

 |  |
| 

[CONTRIBUTING.md](/CopilotKit/OpenGenerativeUI/blob/main/CONTRIBUTING.md "CONTRIBUTING.md")

 | 

[CONTRIBUTING.md](/CopilotKit/OpenGenerativeUI/blob/main/CONTRIBUTING.md "CONTRIBUTING.md")

 | 

[Fix repository links in CONTRIBUTING.md](/CopilotKit/OpenGenerativeUI/commit/1fde890f2b1baa48b8ef79a3204e4075b5ac1299 "Fix repository links in CONTRIBUTING.md
Updated links to use the correct repository name 'OpenGenerativeUI'.")

 |  |
|  |

An open-source showcase for building rich, interactive AI-generated UI with [CopilotKit](https://copilotkit.ai) and [LangChain Deep Agents](https://docs.langchain.com/oss/python/deepagents/overview). Ask the agent to visualize algorithms, create 3D animations, render charts, or generate interactive diagrams — all rendered as live HTML/SVG inside a sandboxed iframe.

OpenGenerativeUI.demo.mp4 3d.airplane.example.mp4

The agent produces **generative UI** — not just text responses, but fully interactive visual components:

- **Algorithm visualizations** — binary search, BFS vs DFS, sorting algorithms
- **3D animations** — interactive WebGL/CSS3D scenes
- **Charts & diagrams** — pie charts, bar charts, network diagrams
- **Interactive widgets** — forms, simulations, math plots

All visuals are rendered in sandboxed iframes with automatic light/dark theming, progressive reveal animations, and responsive sizing.

## Quick Start

```
make setup # Install deps + create .env template
# Edit apps/agent/.env with your real OpenAI API key
make dev # Start all services
```

> **Strong models required.** Generative UI demands high-capability models that can produce complex, well-structured HTML/SVG in a single pass. Set `LLM_MODEL` in your `.env` to one of:
> 
> | Model | Provider |
> | --- | --- |
> | `gpt-5.4` / `gpt-5.4-pro` | OpenAI |
> | `claude-opus-4-6` | Anthropic |
> | `gemini-3.1-pro` | Google |
> 
> Smaller or weaker models will produce broken layouts, missing interactivity, or incomplete visualizations.

- **App**: [http://localhost:3000](http://localhost:3000)
- **Agent**: [http://localhost:8123](http://localhost:8123)

### Available Commands

| Command | Description |
| --- | --- |
| `make setup` | Install all dependencies and create `.env` template |
| `make dev` | Start all services (frontend + agent + mcp) |
| `make dev-app` | Start Next.js frontend only |
| `make dev-agent` | Start LangGraph agent only |
| `make dev-mcp` | Start MCP server only |
| `make build` | Build all apps |
| `make lint` | Lint all apps |
| `make clean` | Clean build artifacts |
| `make help` | Show all available commands |

You can also use `pnpm` directly (`pnpm dev`, `pnpm dev:app`, `pnpm dev:agent`, etc.).

The repo includes a standalone [Model Context Protocol](https://modelcontextprotocol.io) server that exposes the design system, skill instructions, and an HTML document assembler to any MCP-compatible client — including Claude Desktop, Claude Code, and Cursor.

- **`assemble_document` tool** — wraps HTML fragments with the full design system CSS and bridge JS, returning an iframe-ready document
- **Skill resources** — browse and read skill instruction documents (`skills://list`, `skills://{name}`)
- **Prompt templates** — pre-composed prompts for widgets, SVG diagrams, and advanced visualizations

Add to your Claude Desktop config (`claude_desktop_config.json`):

```
{
  "mcpServers": {
 "open-generative-ui": {
 "command": "node",
 "args": ["dist/stdio.js"],
 "cwd": "/path/to/apps/mcp"
 }
  }
}
```

```
# Start the HTTP server
cd apps/mcp && pnpm dev
```

Add to `.mcp.json`:

```
{
  "openGenerativeUI": {
 "url": "http://localhost:3100/mcp"
  }
}
```

See [apps/mcp/README.md](/CopilotKit/OpenGenerativeUI/blob/main/apps/mcp/README.md) for full configuration, Docker deployment, and API reference.

## Architecture

Turborepo monorepo with three packages:

```
apps/
├── app/ Next.js 16 frontend (CopilotKit v2, React 19, Tailwind 4)
├── agent/ Deep Agent (deepagents + CopilotKit middleware, skills-based)
└── mcp/ Standalone MCP server (design system + skills + document assembler)
```

The agent backend uses [LangChain Deep Agents](https://docs.langchain.com/oss/python/deepagents/overview) (`create_deep_agent`) with a skills-based architecture. Instead of injecting all visualization instructions into the system prompt, skills are defined as `SKILL.md` files in `apps/agent/skills/` and loaded on-demand via progressive disclosure:

```
apps/agent/skills/
├── advanced-visualization/SKILL.md # UI mockups, dashboards, Chart.js, generative art
├── master-playbook/SKILL.md # Response philosophy, decision trees, narration patterns
└── svg-diagrams/SKILL.md # SVG generation rules, component patterns, diagram types
```

Deep agents also provide built-in planning (`write_todos`), filesystem tools, and sub-agent support.

1.  **User sends a prompt** via the CopilotKit chat UI
2.  **Deep agent decides** whether to respond with text, call a tool, or render a visual component — consulting relevant skills as needed
3.  **`widgetRenderer`** — a frontend `useComponent` hook — receives the agent's HTML and renders it in a sandboxed iframe
4.  **Skeleton loading** shows while the iframe loads, then content fades in smoothly
5.  **ResizeObserver** inside the iframe reports content height back to the parent for seamless auto-sizing

| Pattern | Hook | Example |
| --- | --- | --- |
| Generative UI | `useComponent` | Pie charts, bar charts, widget renderer |
| Frontend tools | `useFrontendTool` | Theme toggle |
| Human-in-the-loop | `useHumanInTheLoop` | Meeting scheduler |
| Default tool render | `useDefaultRenderTool` | Tool execution status |

| User asks about... | Output type | Technology |
| --- | --- | --- |
| How X works (physical) | Illustrative diagram | SVG |
| How X works (abstract) | Interactive explainer | HTML + inline SVG |
| Process / steps | Flowchart | SVG |
| Architecture / containment | Structural diagram | SVG |
| Database schema / ERD | Relationship diagram | Mermaid |
| Trends over time | Line chart | Chart.js |
| Category comparison | Bar chart | Chart.js |
| Part of whole | Doughnut chart | Chart.js |
| KPIs / metrics | Dashboard | HTML metric cards |
| Design a UI | Mockup | HTML |
| Choose between options | Comparison cards | HTML grid |
| Cyclic process | Step-through | HTML stepper |
| Physics / math | Simulation | Canvas + JS |
| Function / equation | Plotter | SVG + JS |
| Data exploration | Sortable table | HTML + JS |
| Creative / decorative | Art / illustration | SVG |
| 3D visualization | 3D scene | Three.js |
| Music / audio | Synthesizer | Tone.js |
| Network / graph | Force layout | D3.js |
| Quick factual answer | Plain text | None |
| Code solution | Code block | None |
| Emotional support | Warm text | None |

## Tech Stack

Next.js 16, React 19, Tailwind CSS 4, LangChain Deep Agents, LangGraph, CopilotKit v2, Turborepo, Recharts

## License

MIT

## Releases

No releases published

## Packages

No packages published

## Languages

- [TypeScript 73.5%](/CopilotKit/OpenGenerativeUI/search?l=typescript)
- [Python 12.8%](/CopilotKit/OpenGenerativeUI/search?l=python)
- [CSS 12.1%](/CopilotKit/OpenGenerativeUI/search?l=css)
- Other 1.6%