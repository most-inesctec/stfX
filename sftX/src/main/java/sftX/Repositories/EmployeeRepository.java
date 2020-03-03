package sftX.Repositories;

import org.springframework.data.jpa.repository.JpaRepository;
import sftX.Models.Employee.Employee;

/**
 * JPA Repository is the interface responsible for:
 * Creating new instances
 * Updating existing ones
 * Deleting
 * Finding (one, all, by simple or complex properties)
 */
public interface EmployeeRepository extends JpaRepository<Employee, Long> {

}