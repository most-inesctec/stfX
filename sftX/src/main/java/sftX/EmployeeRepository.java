package sftX;

import org.springframework.data.jpa.repository.JpaRepository;

/**
 * JPA Repository is the interface responsible for:
 * Creating new instances
 * Updating existing ones
 * Deleting
 * Finding (one, all, by simple or complex properties)
 */
interface EmployeeRepository extends JpaRepository<Employee, Long> {

}