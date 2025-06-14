# Password-generator-validator
Generate/validate password using exceptions

### Descriptions

1. **Option: Generate Password**
    - User chooses to generate a password with a specified length.
    - The program generates and displays a strong password.
    - The program internally asserts that the generated password meets all validation criteria.
2. **Option: Validate Password**
    - User provides an existing password for validation.
    - The program checks the password against all rules and displays either a success message or specific validation errors.
3. **Error Scenarios**:
    - User enters a non-integer for the password length.
    - User attempts to validate an empty or invalid password.
    - The program handles these errors gracefully and prompts the user again.